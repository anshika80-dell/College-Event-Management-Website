// ================= DARK MODE =================

let darkBtn = document.getElementById("darkModeBtn");

if(darkBtn){

    darkBtn.onclick = function(){

        document.body.classList.toggle("dark");

        if(document.body.classList.contains("dark")){
            darkBtn.innerHTML = "☀️";
        }
        else{
            darkBtn.innerHTML = "🌙";
        }

    };

}



// ================= COUNTDOWN TIMER =================


const eventDate = new Date("September 15, 2026 09:00:00").getTime();


let countdown = setInterval(function(){


    let now = new Date().getTime();

    let distance = eventDate - now;



    if(distance < 0){

        clearInterval(countdown);

        document.getElementById("days").innerHTML="00";
        document.getElementById("hours").innerHTML="00";
        document.getElementById("minutes").innerHTML="00";
        document.getElementById("seconds").innerHTML="00";

        return;

    }



    let days = Math.floor(distance/(1000*60*60*24));


    let hours = Math.floor(
        (distance%(1000*60*60*24))/(1000*60*60)
    );


    let minutes = Math.floor(
        (distance%(1000*60*60))/(1000*60)
    );


    let seconds = Math.floor(
        (distance%(1000*60))/1000
    );



    document.getElementById("days").innerHTML = days;

    document.getElementById("hours").innerHTML = hours;

    document.getElementById("minutes").innerHTML = minutes;

    document.getElementById("seconds").innerHTML = seconds;



},1000);




// ================= REGISTRATION FORM =================



const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        const registration = {
            name: document.getElementById("name").value.trim(),
            email: document.getElementById("email").value.trim(),
            phone: document.getElementById("phone").value.trim(),
            college: document.getElementById("college").value.trim(),
            branch: document.getElementById("branch").value.trim(),
            year: document.getElementById("year").value,
            event: document.getElementById("event").value
        };

        if (Object.values(registration).some(value => !value)) {
            alert("Please fill all the fields.");
            return;
        }

        const submitButton = registerForm.querySelector(
            'button[type="submit"]'
        );

        submitButton.disabled = true;
        submitButton.textContent = "Registering...";

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/api/register/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(registration)
                }
            );

            const result = await response.json();

            if (!response.ok) {
                throw new Error(
                    result.message || "Registration failed."
                );
            }

            alert(result.message);
            registerForm.reset();

        } catch (error) {
            console.error("Registration error:", error);

            alert(
                error.message === "Failed to fetch"
                    ? "Cannot connect to Django. Check that the backend server is running."
                    : error.message
            );

        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Register";
        }
    });
}





// ================= BACK TO TOP BUTTON =================


let topBtn = document.getElementById("topBtn");


if(topBtn){


window.onscroll=function(){


    if(document.documentElement.scrollTop > 200)
    {

        topBtn.style.display="block";

    }

    else
    {

        topBtn.style.display="none";

    }


}



topBtn.onclick=function(){


    window.scrollTo({

        top:0,

        behavior:"smooth"

    });


}


}




// ================= EVENT BUTTONS =================


let eventButtons = document.querySelectorAll(".event-card button");


eventButtons.forEach(function(button){


    button.onclick=function(){

        alert("Event Details Coming Soon!");

    }


});
const menu = document.getElementById("menu-toggle");
const navLinks = document.querySelector(".nav-links");

menu.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});
