$(function() {

  // Submit form action
  $("#formId").submit(function(e) {
    e.preventDefault(); 
    
    $.ajax({
           type: "POST",
           url: "/_predict",
           data: {inpt_model: $("#inpt_model").val(),
                  inpt_beds: $("#inpt_beds").val(),
				  inpt_baths: $("#inpt_baths").val(),
				  inpt_sqft: $("#inpt_sqft").val(),
				  inpt_age: $("#inpt_age").val(),
				  inpt_lotsize: $("#inpt_lotsize").val(),
				  inpt_garages: $("#inpt_garages").val()
           },
           success: function(data)
           {
               $("#house_price").html("$"+data);
               animateCSS('#price_wrapper', 'lightSpeedInLeft');
           }
    });
    
  });
  
  
  $('#deleteUserModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 
    var userId = button.data('user_id')
    var userName = button.data('user_fname')
    var userAge = button.data('user_age')
    var modal = $(this)
    modal.find('.modal-user').text(userName + ' (Age: ' + userAge + ')' )
    
    
    $( "#deleteUserModal button.button-delete" ).click(function(e) {
      //e.preventDefault(); 
    
      $.ajax({
           type: "GET",
           url: "/delete/"+userId,
           success: function(data)
           {
               $('#table_row_userId_'+data).remove();
           }
      });
      
      $('#deleteUserModal').modal("hide");
  
    });
    
    
    
    
  })



  
  
});

