function renderChart(data) {
  const labels = data.map(e => e.date);
  const weights = data.map(e => e.weight);

  const ctx = document.getElementById('weightChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: '体重 (kg)',
        data: weights,
        borderColor: 'blue',
        backgroundColor: 'rgba(0,0,255,0.1)',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: false
        }
      }
    }
  });
}