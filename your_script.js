const map = L.map('map').setView([53.53296196255539, 9.965629577636719], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '© OpenStreetMap'
}).addTo(map);

document.getElementById('getRoute').addEventListener('click', () => {
  const startLat = document.getElementById('startLat').value;
  const startLng = document.getElementById('startLng').value;
  const endLat = document.getElementById('endLat').value;
  const endLng = document.getElementById('endLng').value;

  const apiUrl = `https://api.searoutes.com/route/v2/sea/${startLng}%2C${startLat}%3B${endLng}%2C${endLat}?continuousCoordinates=true&allowIceAreas=false&avoidHRA=false&avoidSeca=false`;

  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      'x-api-key': 'JMURvhdmCk2e7jBcnhuTx4eWp4cCSKzQ7Ukh2cOh'
    }
  };

  fetch(apiUrl, options)
    .then(response => response.json())
    .then(data => {
      // Remove any existing route from the map
      if (window.currentRoute) {
        map.removeLayer(window.currentRoute);
      }

      // Extract coordinates from the response
      const coordinates = data.features[0].geometry.coordinates.map(coord => [coord[1], coord[0]]);

      // Plot the route on the map
      window.currentRoute = L.polyline(coordinates, { color: 'blue' }).addTo(map);

      // Zoom the map to fit the route
      map.fitBounds(window.currentRoute.getBounds());
    })
    .catch(err => console.error(err));
});
