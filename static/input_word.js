function updateLinkAndText() {
  document.getElementById("dynamicText").href = "http://127.0.0.1:5001/api/v1/" + document.getElementById("myInput").value;
  document.getElementById("dynamicText").innerHTML = "http://127.0.0.1:5001/api/v1/" + document.getElementById("myInput").value;
}