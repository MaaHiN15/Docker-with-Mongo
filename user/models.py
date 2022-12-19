from flask import jsonify, request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
from app import db_module

class User_class:
    
    def session_creation(self, user):
        session['logged_in'] = True
        session['data'] = user
        return jsonify({'success': 'User created'})
    
    
    def signup(self):
        user_data = {
            '_id' : uuid.uuid4().hex,
            'name' : request.form.get('name'),
            'email' : request.form.get('email'),
            'password' : request.form.get('password')
        }
        
        user_data['password'] = pbkdf2_sha256.encrypt(user_data['password'])
        
        if db_module.user.find_one({'email' : user_data['email']}):
            return jsonify({'error': 'Existing user'}), 400
        
        if db_module.user.insert_one(user_data):
            return self.session_creation(user_data), 200
        
        
        return jsonify({'error' : 'Not submitted'}), 400
    
    def signout(self):
        session.clear()
        return redirect('/')
 

    def login(self):
        user_allow = db_module.user.find_one({'email' : request.form.get('email')})
        
        if user_allow and pbkdf2_sha256.verify(request.form.get('password'), user_allow['password']):
            return self.session_creation(user_allow), 200
        else:
            return jsonify({'error' : 'Invalid credentials'}), 401