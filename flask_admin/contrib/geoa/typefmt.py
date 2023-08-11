from flask_admin.contrib.sqla.typefmt import DEFAULT_FORMATTERS as BASE_FORMATTERS
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKBElement
from shapely import to_geojson


def geom_formatter(view, value):
    # TODO check srid utility
    if value.srid == -1:
        value.srid = 4326

    r = to_geojson(to_shape(value))
    return to_geojson(to_shape(value))


DEFAULT_FORMATTERS = BASE_FORMATTERS.copy()
DEFAULT_FORMATTERS[WKBElement] = geom_formatter
