/*
Convert the weight to Pokemon
*/
function convert() {
	var pokemon = document.getElementById("pokemon").value;
	var weight = document.getElementById("weight").value;
	if (document.getElementById("units").value === "lbs") {
		weight *= .45359237
	}
	if (weight === 0) {
		document.getElementById("results").innerHTML = "Your weight must be greater than 0!!";
		return;
	}
	$.get({
		url: apiUrl + "pokemon?pokemon=" + pokemon + "&weight=" + weight,
		success: function(data) {
			document.getElementById("results").innerHTML = "You weigh as much as " + data["conversion"] + " " + pokemon + "s!!";
		},
		error: function(data) {
			document.getElementById("results").innerHTML = "That pokemon does not exist!!";
		}
	});
}
