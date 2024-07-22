document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const jsonData = {};
    formData.forEach((value, key) => jsonData[key] = value);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        let output = `
            <h2>Prediction Result</h2>
            <p><strong>Number of Best Friends:</strong> ${jsonData.friends}</p>
            <p><strong>Leadership Experience:</strong> ${jsonData.leadership}</p>
            <p><strong>Hobbies:</strong> ${jsonData.hobbies}</p>
            <p><strong>Inasis:</strong> ${jsonData.inasis}</p>
            <p><strong>Prediction:</strong> ${data.prediction}</p>
        `;
        document.getElementById('output').innerHTML = output;
        document.getElementById('output').style.display = 'block';
        document.getElementById('outputLabel').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});

