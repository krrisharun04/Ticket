const inputs = document.querySelectorAll(".input");
console.log(sessionStorage.summa);
console.log(sessionStorage.summa1);
console.log(sessionStorage.text3);
const count = document.getElementById("count");
let summa = sessionStorage.getItem("summa");
document.getElementById("count").innerHTML = summa;
document.getElementById("tkc").innerHTML = summa;

const total = document.getElementById("total");
let summa1 = sessionStorage.getItem("summa1");
document.getElementById("total").innerHTML = summa1;

sessionStorage.getItem("time");
const time = document.getElementById("time");
time.innerHTML = sessionStorage.time;

// document.getElementById("result").innerHTML=localStorage.getItem("getValue");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});
