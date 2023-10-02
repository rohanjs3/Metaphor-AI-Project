document.getElementById('stockForm').addEventListener('submit', function (e) {
    e.preventDefault();

    let tickers = document.getElementById('tickers').value.split(',').map(ticker => ticker.trim());

    fetch('/add_stocks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tickers: tickers })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
});
// ... [existing code for the stockForm event listener] ...

document.getElementById('getNewsBtn').addEventListener('click', function () {
    fetch('/get_news')
        .then(response => response.json())
        .then(data => {
            let newsContent = "";
            for (let ticker in data) {
                newsContent += `<h3>${ticker}</h3><p>${data[ticker]}</p>`;
            }
            document.getElementById('newsContainer').innerHTML = newsContent;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while fetching news. Please try again.');
        });
});
