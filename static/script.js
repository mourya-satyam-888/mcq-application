var val = 20;

setInterval(function() {
    val--;
    
    
    if (val >= 0) {
        id = document.getElementById("time");
        id.innerHTML = val;
    }
},1000);