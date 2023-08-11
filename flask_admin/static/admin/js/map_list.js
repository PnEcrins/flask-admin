(function ($) {
  const map = initMap("map", {});

  var onEachFeatureCallBack;
  if (typeof onEachFeature == "undefined") {
    onEachFeatureCallBack = function (feature, layer) {
      layer.on({
        click: () => {
          var input_row = $("input[value='" + feature.properties.id + "']");
          const tr = input_row.parent().parent();
          $("tr").css("background-color", "white");
          tr.css("background-color", "yellow");
          // Open popup
          let popupContent = "";
          for (const key in feature.properties) {
            popupContent +=
              "<b>" + key + " : </b>" + feature.properties[key] + " <br>";
          }
          layer.bindPopup(popupContent).openPopup();
        },
      });
    };
  } else {
    onEachFeatureCallBack = onEachFeature;
  }
  geojson = L.geoJSON(geojson_data, { onEachFeature: onEachFeatureCallBack });
  geojson.addTo(map);
  map.fitBounds(geojson.getBounds());
})(jQuery);
