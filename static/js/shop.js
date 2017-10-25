$(document).ready(function ()
{
    $('.productImg').on('click', function() {
     $('.productbig').attr('src', $(this).attr('src'));
     document.getElementById("modalHeader").innerHTML = $(this).attr('alt');
     $('#productmodal').modal('show');   
    }); 
    });
