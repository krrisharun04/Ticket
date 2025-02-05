const $btnPrint = document.querySelector("#btnPrint");

$btnPrint.addEventListener("click", () => {
    window.print();
});
const count = document.getElementById("count");
let summa = sessionStorage.getItem("summa");
document.getElementById("count").innerHTML = summa;
const total = document.getElementById("total");
let summa1 = sessionStorage.getItem("summa1");
document.getElementById("total").innerHTML = summa1;

sessionStorage.getItem("time");
const time = document.getElementById("time");
time.innerHTML = sessionStorage.time;
