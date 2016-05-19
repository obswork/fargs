$("#sendMessage").click(function(e){
    e.preventDefault();
    var contactMessage = $("#contactForm").serialize();
    $.ajax({
        type: "POST",
        url: "/",
        data: contactMessage,
        success: function(data){
            if(data.success){
                $('#contactForm')[0].reset();
                $("#contactForm").find(".error").remove();
                $("#contactForm").before('<div class="alert success">' + data.success + '</div>');
                setTimeout(function(){
                    $(".success").fadeOut("slow");
                }, 6000);
            }else{
                $("#contactForm").find(".error").remove();
                for (var key in data) {
                    // alt. implementation so keys don't need to be specified - if (value NOT == '' for key in data: {key:value}) ..or something like that
                    if (key in {email: 1, message: 1, number: 1, sender: 1, }) {
                        error = data[key][0];
                        field = $("#contactForm").find("#id_" + key);
                        field.after('<div class="alert error">' + error + '</div>');
                    }
                }
            }
        }
    });
});
$("#clear").click(function(e){
    $("#contactForm").find(".error").remove();
});
