$(".estimator-input").change(function() {
    var rooms = $("#rooms").val();
    var couches = $("#couches").val();
    var loveseats = $("#loveseats").val();
    // var recurrence = $("#recurrence").val();
    // 5% discount = .95*estimate
    var discount = '.05';
    var prices = {room_price:35, couch_price:75, loveseat_price:50};
    var estimate = rooms*prices.room_price + couches*prices.couch_price + loveseats*prices.loveseat_price;
    /* if(recurrence>1){
        estimate = estimate*(1-discount)*recurrence;
    }
    */
    $("#one-time-total").html(estimate);
});

$("#id_name").attr("placeholder", "Name");
$("#id_number").attr("placeholder", "Number");
$("#id_email").attr("placeholder", "Email");
$("#id_message").attr("placeholder", "Message");
