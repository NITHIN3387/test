function onClickedPredict() {
    var N_value = document.getElementById("N_value").value;
    var P_value = document.getElementById("P_value").value;
    var K_value = document.getElementById("K_value").value;
    var Season = document.getElementById("Season").value;
    var prediction = document.getElementById("prediction");
  
    var url = "http://127.0.0.1:5000/predict";
  
    $.post(url, {
        N_value,
        P_value,
        K_value,
        Season
    },function(data, status) {
        console.log(data.estimated_price);
        prediction.innerHTML = "<h2>" + data.prediction.toString() + "</h2>";
        console.log(status);
    });
}