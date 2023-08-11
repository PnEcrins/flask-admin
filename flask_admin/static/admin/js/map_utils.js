function initMap(htmlElementId, config) {
  // if (!window.TILE_LAYER_ATTRIBUTION) {
  //   console.error(
  //     "You must set FLASK_ADMIN_TILE_LAYER_URL in your Flask settings to use the geo widgets"
  //   );
  //   return false;
  // }
  // if (!window.DEFAULT_CENTER_LAT || !window.DEFAULT_CENTER_LONG) {
  //   console.error(
  //     "You must set DEFAULT_CENTER_LAT and DEFAULT_CENTER_LONG in your Flask settings to use the map widget"
  //   );
  //   return false;
  // }

  // var center = null;
  // if (config["lat"] && config["lng"]) {
  //   center = L.latLng($el.data("lat"), $el.data("lng"));
  // }
  // var maxBounds = null;
  // if (
  //   config["max-bounds-sw-lat"] &&
  //   config["max-bounds-sw-lng"] &&
  //   config["max-bounds-ne-lat"] &&
  //   config["max-bounds-ne-lng"]
  // ) {
  //   maxBounds = L.latLngBounds(
  //     L.latLng(config["max-bounds-sw-lat"], config["max-bounds-sw-lng"]),
  //     L.latLng(config["max-bounds-ne-lat"], config["max-bounds-ne-lng"])
  //   );
  // }
  // var mapOptions = {
  //   center: center,
  //   zoom: config.zoom || 12,
  //   minZoom: config["min-zoom"],
  //   maxZoom: config["max-zoom"],
  //   maxBounds: maxBounds,
  // };
  //TODO MAP OPTIONS
  var map = L.map(htmlElementId).setView([51.505, -0.09], 13);
  L.tileLayer(window.TILE_LAYER_URL, {
    attribution: window.TILE_LAYER_ATTRIBUTION,
    maxZoom: 18,
  }).addTo(map);
  return map;
}
