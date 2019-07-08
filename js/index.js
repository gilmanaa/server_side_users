var newUser = $("#newUser");
var messages = $("#messages")
var getUsers = $("#getUsers");
var addUser = $("#addUser");
var delUser = $("#delUser");
var users = $("#users")

getUsers.click(function(){
    users.text("Current Users:");
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/getUsers",
        dataType: "JSON",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var username = response[i];
                var seperator = $("<div>");
                seperator.addClass("current-users")
                seperator.append(username);
                users.append(seperator);
            }
        },
        error: function(response) {
            //console.log(response)
        },
        complete: function(response,status) {
            //console.log(response)
        }
    })
})

addUser.click(function(){
    $.ajax({
        type: "POST",
        url: "http://localhost:7000/addUser",
        data: {
            user: newUser.val()
        },
        success: function(response) {
            messages.text(JSON.parse(response).msg)
        }
    })
})

delUser.click(function(){
    $.ajax({
        type: "POST",
        url: "http://localhost:7000/delUser",
        data: {
            user: newUser.val()
        },
        success: function(response) {
            messages.text(JSON.parse(response).msg)
        }
    })
})