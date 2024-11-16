function onClickedPredictDisease() {
  console.log("Predict disease button clicked");

  var jaundice = document.querySelector('input[name="uijaundice"]:checked').value == 2 ? 0 : 1;
  var fatigue = document.querySelector('input[name="uiFatigue"]:checked').value == 2 ? 0 : 1;
  var discomfort = document.querySelector('input[name="uiDiscomfort"]:checked').value == 2 ? 0 : 1;
  var appetite = document.querySelector('input[name="uiAppetite"]:checked').value == 2 ? 0 : 1;
  var urine = document.querySelector('input[name="uiUrine"]:checked').value == 2 ? 0 : 1;
  var itchySkin = document.querySelector('input[name="uiItchySkin"]:checked').value == 2 ? 0 : 1;
  var bruising = document.querySelector('input[name="uiBruising"]:checked').value == 2 ? 0 : 1;
  var nauseaVomiting = document.querySelector('input[name="uiNauseaVomiting"]:checked').value == 2 ? 0 : 1;
  var smokingStatus = document.querySelector('input[name="uiSmokingStatus"]:checked').value;
  var alcoholConsumption = document.querySelector('input[name="uiAlcoholConsumption"]:checked').value;

  // Map values for alcohol consumption and smoking status
  if (alcoholConsumption === 'frequent') {
    alcoholConsumption = 1;
  } else if (alcoholConsumption === 'sometimes') {
    alcoholConsumption = 2;
  } else {
    alcoholConsumption = 0;
  }

  if (smokingStatus === 'frequent') {
    smokingStatus = 1;
  } else if (smokingStatus === 'sometimes') {
    smokingStatus = 2;
  } else {
    smokingStatus = 0;
  }

  var url = "http://127.0.0.1:5000/predict_disease";

  $.ajax({
    url: url,
    method: "POST",
    contentType: "application/json",  // Set the correct content type for JSON
    data: JSON.stringify({
        jaundice: jaundice,
        fatigue: fatigue,
        discomfort: discomfort,
        appetite: appetite,
        urine: urine,
        itchySkin: itchySkin,
        bruising: bruising,
        nauseaVomiting: nauseaVomiting,
        smokingStatus: smokingStatus,
        alcoholConsumption: alcoholConsumption
    }), // Convert data to JSON string
    success: function (data, status) {
        console.log(data.estimated_disease);
        var estDisease = document.getElementById("uiEstimatedDisease");
        estDisease.innerHTML = "<h2>" + (data.estimated_disease?"Danger!!":"Safe :)") + "</h2>";
        console.log(status);
    },
    error: function (xhr, status, error) {
        console.log("Error:", error);
        console.log("Response:", xhr.responseText);
    }
});

}

function onClickedPredictImage() {
  console.log("Predict image disease button clicked");
 
  var fileInput = document.getElementById('imageUpload');
  var file = fileInput.files[0];
  if (!file) {
     alert("Please select an image file.");
     return;
  }
 
  var formData = new FormData();
  formData.append('file', file);
 
  var url = "http://127.0.0.1:5000/predict_image_disease";
 
  $.ajax({
     url: url,
     type: 'POST',
     data: formData,
     processData: false,
     contentType: false,
     success: function (data) {
       console.log(data.predicted_result);
       var estDisease = document.getElementById("uiEstimatedImageDisease");
       var out = "";
       if(data.predicted_result) out = "Danger!!"
       else out = "Safe :)"
       console.log("again")
       console.log(out)
       estDisease.innerHTML = "<h2>" + out + "</h2>";
     },
     error: function (error) {
       console.error("Error:", error);
     }
  });
 }