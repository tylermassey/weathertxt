var valid = [false,false,false];
var remove = false;

function checkNumber(form,value) {
    if(value) {
        var m = value.match(/\d/g);
        if(!(m && m.length === 10)) {
            if(form==1) {
                document.getElementById("phoneError1").style.display = "block";
                valid[0] = false;
            }
            else if(form==2) {
                document.getElementById("phoneError2").style.display = "block";
                remove = false;
            }
        }
        else {
            if(form==1) {
                document.getElementById("phoneError1").style.display = "none";
                valid[0] = true;
            }
            else if(form==2) {
                document.getElementById("phoneError2").style.display = "none";
                remove = true;
            }
        }
    }
}

function checkZipcode(value) {
    if(value) {
        var m = value.match(/\d/g);
        if(!(m && m.length === 5)) {
            document.getElementById("zipcodeError").style.display = "block";
            valid[1] = false;
        }
        else {
            document.getElementById("zipcodeError").style.display = "none";
            valid[1] = true;
        }
    }
}

function checkTime(value) {
    if(!value) {
        document.getElementById("timeError").style.display = "block";
        valid[2] = false;
    }
    else {
        document.getElementById("zipcodeError").style.display = "none";
        valid[2] = true;
    }
}

function validateForm(form) {
    if(valid[0] && valid[1] && valid[2])
        form.submit();
    else
        return false;
}

function validateDelete(form) {
    if(remove)
        form.submit();
    else
        return false;    
}