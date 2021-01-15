$(document).on('submit', '#addcomment', function(e){
    e.preventDefault()
    var id = $(this).data('id')
    $.ajax({
        type: "POST", //ở đây là dạng method GET hoặc POST
        url: "/product/"+id+"/addcomment/",  //url 
        data:  $("#addcomment").serialize(), 
        dataType: 'html', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng html
        success: function  (data, textStatus, jqXHR) {
            $("#listcomment").html(data)
            $("#addcomment")[0].reset()
        }
    });
})
