function sendEmail() {
    var xmlHttp = new XMLHttpRequest();
    var name = document.getElementById("name").value;
    var number = document.getElementById("number").value;
    var location = document.getElementById("location").value;
    var email = document.getElementById("email").value;

    if (name == "" || number == "" || location == "" || email == "") {
        window.alert("Please fill required fields.");
    } else {
        xmlHttp.open("GET", "http://127.0.0.1:5000/submit/" + name + "/" + number + "/" + location + "/" + email, false);
        xmlHttp.send(null);
        window.alert("Your data was successfully saved.");
        window.location.reload();
    }

    return xmlHttp.responseText;
}