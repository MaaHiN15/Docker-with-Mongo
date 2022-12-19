$("form[name=form").submit(function(e){
    let $form = $(this);
    let $error = $form.find('.error');
    let data = $form.serialize();

    $.ajax({
        url: "/user/signup/",
        type : "POST",
        data : data,
        dataType : "json",
        success : function(res){
            window.location.href = '/dashboard/';
        },
        error : function(res){
            $error.text(res.responseJSON.error).removeClass('error--hidden');
        }
    })


    e.preventDefault();
});$("form[name=login-form").submit(function(e){
    let $form = $(this);
    let $error = $form.find('.error');
    let data = $form.serialize();

    $.ajax({
        url: "/user/login/",
        type : "POST",
        data : data,
        dataType : "json",
        success : function(res){
            window.location.href = '/dashboard/';
        },
        error : function(res){
            $error.text(res.responseJSON.error).removeClass('error--hidden');
        }
    })


    e.preventDefault();
});