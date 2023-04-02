document.querySelector(".switch").addEventListener("click", event => {
    event.currentTarget.classList.toggle("switched");
});

for (const element of document.querySelectorAll(".post-preview")) {
    element.addEventListener("click", setActive);
}
let currentActivePostElement = null;
// document.getElementById(id).style.visibility = "hidden";
function setActive(event) {
        var z, i, elmnt, file, xhttp, pid;
        if(currentActivePostElement !== null) {
            currentActivePostElement.style.display = "none";
        }
        pid = event.currentTarget.getAttribute("pid");
        const ul = event.currentTarget.nextElementSibling;
        ul.style.display = "";
        console.log(ul);
        /*search for elements with a certain atrribute:*/
        const theUrl = "/forumleftrep/"+ pid;
        /* Make an HTTP request using the attribute value as the file name: */

        fetch(theUrl, {method: "GET"})
                .then(response => response.text())
                .then(text => {
                    ul.innerHTML = text;
                })
        // var xmlHttp = new XMLHttpRequest();
        // xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
        // xmlHttp.send( null );
        // ul.innerHTML = this.responseText;
        currentActivePostElement = ul;

        return;

          }

//set text values