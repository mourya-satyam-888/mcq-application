var val = 20;

setInterval(function() {   
    let que = document.getElementById("que").value;
    
    if (que == 5) {
        id = document.getElementById("next");
        id.innerHTML = "submit";
    }
    
},1);

setInterval(function() {
    val--;
    
    
    if (val >= 0) {
        id = document.getElementById("time");
        id.innerHTML = val;
    }
    
    if (val == 0) {
        function next() {
            document.getElementById("next").click();
        }
        next();
    }
    
    let que = document.getElementById("que").value;
    
    if (que == 5) {
        id = document.getElementById("next");
        id.innerHTML = "submit";
    }
    
},1000);