function fetchAndSetAircrafts(layerGroup) {
    console.log("Demo!")
    $.get("/api/aircrafts?lat=51.5005&lon=-0.1145").then(data => {
        // Clear all layers (airliners) before adding new ones
        layerGroup.clearLayers()

        const aircrafts = data['ac']
        aircrafts.forEach(aircraft => {
            L.marker(
                [aircraft["lat"], aircraft["lon"]],
                { icon: airlinerIcon, rotationAngle: aircraft['nav_heading'] })
                .bindTooltip(aircraft['flight'])
                .addTo(layerGroup);
        })
    }
    )
}