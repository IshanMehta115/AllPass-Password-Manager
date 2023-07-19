const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))



const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
function generatePassword(length) {
    // define all possible characters

    // initialize password variable

    let password = "";

    // create random password
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }

    let c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    for (let i = 0; i < length; i++) {
        for (let j = 0; j < 26; j++) {
            if (chars[j] == password[i]) c1++;
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


function suggest_password(field_ids) {
    pswd = generatePassword(18)
    for (var i = 0; i < field_ids.length; i++) {
        document.getElementById(field_ids[i]).value = pswd;
    }
}


function toggle_visibility(cb_id, field_ids) {
    let new_type;
    if (document.getElementById(cb_id).checked) {
        new_type = 'text';
    } else {
        new_type = 'password';
    }
    for (var i = 0; i < field_ids.length; i++) {
        document.getElementById(field_ids[i]).type = new_type;
    }
}


function toggle_display(eleid) {
    var display_button = document.getElementById(eleid);
    var about_info = document.getElementById('about_info');
    var password_details = document.getElementById('password_details');
    if (display_button.textContent == "About the app") {
        display_button.textContent = "My passwords";
        about_info.classList.remove("visually-hidden");
        password_details.classList.add("visually-hidden");
    }
    else {
        display_button.textContent = "About the app";
        about_info.classList.add("visually-hidden");
        password_details.classList.remove("visually-hidden");
    }
}

function copy_to_clipboard(eleid) {
    var copyText = document.getElementById(eleid);
    before = copyText.type
    copyText.type = 'text';
    copyText.select();
    document.execCommand("copy");
    copyText.type = before;
}


function set_password_val(val) {
    var ele = document.getElementById('confirm_delete_modal_password_val');
    ele.value = val
}

function fill_values(name, email, password, hash_val) {
    document.getElementById("application_name_input_modify_password").value = name;
    document.getElementById("email_input_modify_password").value = email;
    document.getElementById("password_input_modify_password").value = password;
    document.getElementById("val_input_modify_password").value = hash_val;
}



function check_text(value){
    var verdict = true;
    if(value.length < 5)
    {
        verdict = false;
    }
    for(var i=0;i<value.length;i++)
    {
        if (!(('0' <= value[i] && value[i] <= '9') || ('a' <= value[i] && value[i] <= 'z') || ('A' <= value[i] && value[i] <= 'Z')))
        {
            verdict = false;
            break;
        }
    }
    return verdict
}
function check_search_text(value) {
    var verdict = true;
    for (var i = 0; i < value.length; i++) {
        if (!(('0' <= value[i] && value[i] <= '9') || ('a' <= value[i] && value[i] <= 'z') || ('A' <= value[i] && value[i] <= 'Z'))) {
            verdict = false;
            break;
        }
    }
    return verdict
}
function check_password(value) {
    var verdict = true;
    if (value.length < 18) {
        verdict = false;
    }
    let c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    for (let i = 0; i < value.length; i++) {
        for (let j = 0; j < 26; j++) {
            if (chars[j] == value[i]) c1++;
        }
        for (let j = 26; j < 52; j++) {
            if (chars[j] == value[i]) c2++;
        }
        for (let j = 52; j < 62; j++) {
            if (chars[j] == value[i]) c3++;
        }
        for (let j = 62; j < 72; j++) {
            if (chars[j] == value[i]) c4++;
        }
    }
    console.log(c1);
    console.log(c2);
    console.log(c3);
    console.log(c4);
    if(0==c1 || 0==c2 || 0==c3 || 0==c4) verdict = false;
    return verdict
}
function check_login_modal() {
    var username_input_login = document.getElementById('username_input_login');
    var ok = check_text(username_input_login.value)
    if(!ok)
    {
        $('#username_input_login').tooltip('show');
        return;
    }
    var password_input_login = document.getElementById('password_input_login');
    var ok = check_password(password_input_login.value)
    if (!ok) {
        $('#password_input_login').tooltip('show');
        return;
    }
    document.getElementById('login_continue').click();
}


function check_password2(pswd1, pswd2){
    return pswd1==pswd2;
}
function check_email(value) {
    if(value.length==0) return false;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(value);
}


function check_signup_modal() {
    var username_input_signup = document.getElementById('username_input_signup');
    var ok = check_text(username_input_signup.value)
    if (!ok) {
        $('#username_input_signup').tooltip('show');
        return;
    }

    var email_input_signup = document.getElementById('email_input_signup');
    var ok = check_email(email_input_signup.value)
    if (!ok) {
        $('#email_input_signup').tooltip('show');
        return;
    }

    var password_input_signup = document.getElementById('password_input_signup');
    var ok = check_password(password_input_signup.value)
    if (!ok) {
        $('#password_input_signup').tooltip('show');
        return;
    }

    var password2_input_signup = document.getElementById('password2_input_signup');
    var ok = check_password2(password_input_signup.value,password2_input_signup.value)
    if (!ok) {
        $('#password2_input_signup').tooltip('show');
        return;
    }


    document.getElementById('signup_continue').click();
}


function check_add_password_modal() {
    var application_name_input_add_password = document.getElementById('application_name_input_add_password');
    var ok = check_text(application_name_input_add_password.value)
    if (!ok) {
        $('#application_name_input_add_password').tooltip('show');
        return;
    }

    var email_input_add_password = document.getElementById('email_input_add_password');
    var ok = check_email(email_input_add_password.value)
    if (!ok) {
        $('#email_input_add_password').tooltip('show');
        return;
    }

    var password_input_add_password = document.getElementById('password_input_add_password');
    var ok = check_password(password_input_add_password.value)
    if (!ok) {
        $('#password_input_add_password').tooltip('show');
        return;
    }

    document.getElementById('add_password_continue').click();
}


function check_modify_password_modal() {

    var application_name_input_modify_password = document.getElementById('application_name_input_modify_password');
    var ok = check_text(application_name_input_modify_password.value)
    if (!ok) {
        $('#application_name_input_modify_password').tooltip('show');
        return;
    }

    var email_input_modify_password = document.getElementById('email_input_modify_password');
    var ok = check_email(email_input_modify_password.value)
    if (!ok) {
        $('#email_input_modify_password').tooltip('show');
        return;
    }

    var password_input_modify_password = document.getElementById('password_input_modify_password');
    var ok = check_password(password_input_modify_password.value)
    if (!ok) {
        $('#password_input_modify_password').tooltip('show');
        return;
    }
    document.getElementById('modify_password_continue').click();
}


function check_password_modal(){
    var email_input_password_reset = document.getElementById('email_input_password_reset');
    var ok = check_email(email_input_password_reset.value)
    if (!ok) {
        $('#email_input_password_reset').tooltip('show');
        return;
    }
    document.getElementById('password_reset_continue').click();
}


function check_change_password_modal(){


    var password_input_change_password = document.getElementById('password_input_change_password');
    var ok = check_password(password_input_change_password.value)
    if (!ok) {
        $('#password_input_change_password').tooltip('show');
        return;
    }

    var password2_input_change_password = document.getElementById('password2_input_change_password');
    var ok = check_password2(password_input_change_password.value, password2_input_change_password.value)
    if (!ok) {
        $('#password2_input_change_password').tooltip('show');
        return;
    }
    document.getElementById('change_password_continue').click();
}

function check_search_bar(){
    var search_bar_id = document.getElementById('search_bar_id');
    var ok = check_search_text(search_bar_id.value)
    if (!ok) {
        $('#search_bar_id').tooltip('show');
        return;
    }
    document.getElementById('search_button').click();
}






