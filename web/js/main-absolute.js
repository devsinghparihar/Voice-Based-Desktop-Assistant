eel.expose(currentStatus);
function currentStatus(text){
document.getElementById("statusBar").innerHTML =text;
}

eel.expose(closeWin);
function closeWin(){
window.close();
}

function myFunc(){
 eel.starter();   
 eel.assistant();

}
eel.expose(tester);
function tester(text){
    document.getElementById("test").innerText = text
}