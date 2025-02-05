const container = document.querySelector(".container");
const seats = document.querySelectorAll(".row .seat:not(.occupied)");
var count = document.getElementById("count");
var total = document.getElementById("total");
const movieSelect = document.getElementById("movie");

let ticketPrice = parseInt(movieSelect.value);

function updateSelectedCount() {
  var selectedSeats = document.querySelectorAll(".row .selected");
  var selectedSeatsCount = selectedSeats.length;
  count.innerHTML = selectedSeatsCount;
  total.innerHTML = selectedSeatsCount * ticketPrice;

  const span = document.getElementById('count');
  const text1 = span.textContent;
  console.log(text1);

  const span1 = document.getElementById('total');
  const text2 = span1.textContent;
  console.log(text2);


  sessionStorage.setItem("summa",text1);
  sessionStorage.setItem("summa1",text2);

  var getValue = document.getElementById("time").selectedOptions[0].value;
  sessionStorage.setItem("time", getValue);
  console.log(getValue);
  
  // var getValue = document.getElementById("time").selectedOptions[0].value;
  // const text3 = getValue.textContent;
  // sessionStorage.setItem("summa2",text3);
  // console.log(getValue);
  

  // var amount = selectedSeatsCount * ticketPrice;
  // total.innerHTML = amount;

  // "{{ myVar }}"=total
  // localStorage.setItem("myValue", amount);
  // console.log(count,total);
}
// function passvalue()
// {
//   var firstname=document.getElementById("txt").value;
//   localStorage.setItem("textvalue",firstname);
//   return false;
// }

movieSelect.addEventListener("change", (e) => {
  ticketPrice = parseInt(e.target.value);
  updateSelectedCount();
});

container.addEventListener("click", (e) => {
  console.log(e);
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("occupied")
  ) {
    e.target.classList.toggle("selected");
    updateSelectedCount();
  }
});
