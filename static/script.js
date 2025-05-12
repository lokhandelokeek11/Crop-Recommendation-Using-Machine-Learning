document.addEventListener("DOMContentLoaded", function () {
    console.log("Page Loaded Successfully");

    document.getElementById("predictForm").addEventListener("submit", async function(event) {
        event.preventDefault();

        const formData = {
            N: document.getElementById("N").value,
            P: document.getElementById("P").value,
            K: document.getElementById("K").value,
            temperature: document.getElementById("temperature").value,
            humidity: document.getElementById("humidity").value,
            ph: document.getElementById("ph").value,
            rainfall: document.getElementById("rainfall").value
        };

        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        if (result.recommended_crop) {
            document.getElementById("result").innerText = "Recommended Crop: " + result.recommended_crop;
        } else {
            document.getElementById("result").innerText = "Error: " + result.error;
        }
    });
});
