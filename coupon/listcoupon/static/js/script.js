$(document).ready(function(){
 $('#group-filter li').click(function() {
 $('.active').removeClass('active');
 $(this).addClass('active');
 var type1 = $(this).attr('data-type');
// alert("OK! "+ type);
$.ajax(
    {
        type:"GET",
        url: "/home",
        data:{
                 type: type1
        },
        success: function( data )
        {
            alert("thanh cong");

        }
     })
});

  $(".code-hide").click(function(){
    var voucher = $(this).find(".voucher-item-code").val();
    alert(voucher);
    $(".mfp-content .code-text").val( voucher );
    $("#myModal").modal();
  });
});

