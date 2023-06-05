//display  modal on click

const modalWrapper = document.querySelector(".modals-wrapper");
function close_login(){
    const modal = document.getElementById("login-modal");
    modal.style.display = "none";
    document.querySelector("header").style.display = "unset";
}

if (modalWrapper) {
    function displayModal(id) {
        const modal = document.getElementById(id);
        modalWrapper.style.display = "flex";
        modal.style.display = "flex";
        const features = document.getElementById("home-modal");
        if(features!=null) features.style.display = "none";
        //close modal
        const close = document.getElementById("close-modal");
        close.addEventListener("click", () => {
            modalWrapper.style.display = "none";
            modal.style.display = "none";
            if (features != null) features.style.display = "flex";
            //I added this later, didn't cover it on the tutorial
            document.querySelector("header").style.display = "unset";
        })

        //I added this later, didn't cover it on the tutorial
        document.querySelector("header").style.display = "none";
    }
}

function fill_values(url,email,password,hash_val){
    document.getElementById("apurl2").value = url;
    document.getElementById("apemail2").value = email;
    document.getElementById("add_pswd_pswd2").value = password;
    document.getElementById("mpid").value = hash_val;
}

function generatePassword(length) {
    // define all possible characters
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";

    // initialize password variable
    
    let password = "";

    // create random password
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }

    let c1=0,c2=0,c3=0,c4=0;
    for(let i=0;i<length;i++){
        for(let j=0;j<26;j++){
            if(chars[j]==password[i]) c1++;
        }
        for (let j = 26; j < 52; j++) {
            if (chars[j] == password[i]) c2++;
        }
        for (let j = 52; j < 62; j++) {
            if (chars[j] == password[i]) c3++;
        }
        for (let j = 62; j < 72; j++) {
            if (chars[j] == password[i]) c4++;
        }
    }
    if (!c1) { password += chars[Math.floor(Math.random() * 26) + 0] };
    if (!c2) { password += chars[Math.floor(Math.random() * 26) + 26] };
    if (!c3) { password += chars[Math.floor(Math.random() * 10) + 52] };
    if (!c4) { password += chars[Math.floor(Math.random() * 10) + 62] };
    return password;
}

function copy1(eleid) {
    console.log(eleid)
    var copyText = document.getElementById(eleid);
    before = copyText.type 
    copyText.type = 'text';
    copyText.select();
    document.execCommand("copy");
    copyText.type = before;
}



function toggle_visibility1() {
    var e1 = document.getElementById("add_pswd_pswd");
    var e2 = document.getElementById("tv1");
    if (e1.type == "text") {
        e1.type = 'password';
        e2.value = "show password"
    }
    else {
        e1.type = "text"
        e2.value = "hide password"
    }
}

function suggest_password1() {
    var e = document.getElementById("add_pswd_pswd");
    e.value = generatePassword(20)
}

function toggle_visibility12() {
    var e1 = document.getElementById("add_pswd_pswd2");
    var e2 = document.getElementById("tv12");
    if (e1.type == "text") {
        e1.type = 'password';
        e2.value = "show password"
    }
    else {
        e1.type = "text"
        e2.value = "hide password"
    }
}

function suggest_password12() {
    var e = document.getElementById("add_pswd_pswd2");
    e.value = generatePassword(20)
}


function toggle_visibility2() {
    var e1 = document.getElementById("signup_pswd1");
    var e2 = document.getElementById("signup_pswd2");
    var e3 = document.getElementById("tv2");
    if (e1.type == "text") {
        e1.type = 'password';
        e2.type = "password"
        e3.value = "show password"
    }
    else {
        e1.type = 'text';
        e2.type = "text"
        e3.value = "hide password"
    }
}


function toggle_display(id1,id2,id3,id4) {
    var e1 = document.getElementById(id1);
    var e2 = document.getElementById(id2);
    var e3 = document.getElementById(id3);
    var e4 = document.getElementById(id4);
    console.log("here");
    if (e1.style.display == "none") {
        console.log("if");
        e1.style.display = "flex";
        e2.style.display = "none";
        e4.style.display = "none";
        e3.textContent = "My passwords";
    }
    else {
        console.log("else");
        e1.style.display = "none";
        e2.style.display = "grid";
        e4.style.display = "";
        e3.textContent = "About the app";
    }
}

function suggest_password2() {
    var e1 = document.getElementById("signup_pswd1");
    var e2 = document.getElementById("signup_pswd2");
    pswd = generatePassword(20)
    e1.value = pswd
    e2.value = pswd
}



function toggle_visibility3() {
    var e1 = document.getElementById("psr_pswd1");
    var e2 = document.getElementById("psr_pswd2");
    var e3 = document.getElementById("tv3");
    if (e1.type == "text") {
        e1.type = 'password';
        e2.type = "password";
        e3.value = "show password";
    }
    else {
        e1.type = 'text';
        e2.type = "text";
        e3.value = "hide password";
    }
}

function toggle_visibility(eleid,tv32){
    var e1 = document.getElementById(eleid);
    var e3 = document.getElementById(tv32);
    if (e1.type == "text") {
        e1.type = 'password';
        e3.value = "show password";
    }
    else {
        e1.type = 'text';
        e3.value = "hide password";
    }
}

function suggest_password3() {
    var e1 = document.getElementById("psr_pswd1");
    var e2 = document.getElementById("psr_pswd2");
    pswd = generatePassword(20)
    e1.value = pswd
    e2.value = pswd
}



const actions = document.querySelectorAll(".actions");
if (actions) {
    actions.forEach(action => {
        action.onclick = () => {
            const links = action.querySelectorAll("a");
            links.forEach(link => {
                link.style.display = "flex";
            })
            setTimeout(function () {
                links.forEach(link => {
                    link.style.display = "none";
                })
            }
                , 3000)
        }
    })
}


function email_validity(eleid) {
    ele = document.getElementById(eleid);
    if (!ele.validity.valid) {
        ele.setCustomValidity("Enter a valid email");
        ele.reportValidity();
        setTimeout(function () {
            ele.setCustomValidity("");
        }, 7000);
    }
};

function password_validity(eleid) {
    ele = document.getElementById(eleid);
    if (!ele.validity.valid) {
        ele.setCustomValidity("Enter a valid password.Atleast one small/capital letter.Atleast one digit.Atleast one special character.Allowed speical characters are !@#$%^&*().Atleast 10 characters long");
        ele.reportValidity();
        setTimeout(function () {
            ele.setCustomValidity("");
        }, 7000);
    }
};

function url_validity(eleid) {
    ele = document.getElementById(eleid);
    if (!ele.validity.valid) {
        rv1.setCustomValidity("Enter a valid url. Use https:\\\\prefix");
        ele.reportValidity();
        setTimeout(function () {
            ele.setCustomValidity("");
        }, 3000);
    }
};


function username_validity(eleid) {
    ele = document.getElementById(eleid);
    if (!ele.validity.valid) {
        rv6.setCustomValidity("Enter a valid username.Only alphabets and digits allowed. Minimum length should be 5 characters");
        ele.reportValidity();
        setTimeout(function () {
            ele.setCustomValidity("");
        }, 7000);
    }
};
