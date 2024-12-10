document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const spinner = document.getElementById('loadingSpinner');
    form.onsubmit = function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        spinner.style.display = 'block'; // Show spinner when request starts
        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Delay the display of results by 20 seconds
            setTimeout(() => {
                spinner.style.display = 'none'; // Hide spinner when data is ready to display
                const results = document.getElementById('results');
                results.innerHTML = ''; // Clear previous results
                for (const [email, score] of Object.entries(data)) {
                    const resultItem = document.createElement('div');
                    resultItem.classList.add('result-item');
                    resultItem.innerHTML = `<strong>Email:</strong> ${email}<br><strong>Score:</strong> ${score}`;
                    results.appendChild(resultItem);
                }
            }, 20000); // 20000 milliseconds delay
        })
        .catch(error => {
            console.error('Error:', error);
            spinner.style.display = 'none'; // Ensure spinner is hidden on error
        });
    };
});
