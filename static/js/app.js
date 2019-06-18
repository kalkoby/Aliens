// from data.js
var tableData = data;
var submit = d3.select("#submit");

// You can also define the click handler inline
submit.on("click", function() {
    d3.event.preventDefault();

    var inputElement= d3.select("#date-input");
    var inputValue = inputElement.property("value")
    
    
    console.log(inputValue);
    // console.log("Hi, a button was clicked!");
    // console.log(d3.event.target);

    var filteredData = tableData.filter(tData => tData.datetime === inputValue);
    
    var tbody = d3.select("tbody");
    console.log(filteredData);
    filteredData.forEach((alienReport) => {
        var row = tbody.append("tr");
        Object.entries(alienReport).forEach(([key, value]) => {
          var cell = row.append("td");
          cell.text(value);
        });
    });
    // d3.select("h1>span").text(inputValue);

}); 
// inputField.on("change", function() {
//         var newText = d3.event.target.value;
//         console.log(newText);
//     });
// var tbody = d3.select("tbody");
// console.log(filteredData)
// data.forEach((alienReport) => {
//     var row = tbody.append("tr");
//     Object.entries(alienReport).forEach(([key, value]) => {
//       var cell = row.append("td");
//       cell.text(value);
//     });
// });