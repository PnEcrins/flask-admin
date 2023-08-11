# Create dummy secrey key so we can use sessions
SECRET_KEY = "123456790"

# database connection
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://flask_admin_geo:flask_admin_geo@localhost/flask_admin_geo"
)
SQLALCHEMY_ECHO = True

# credentials for loading map tiles from mapbox
MAPBOX_MAP_ID = "..."
MAPBOX_ACCESS_TOKEN = "..."

# when the creating new shapes, use this default map center
DEFAULT_CENTER_LAT = -33.918861
DEFAULT_CENTER_LONG = 18.423300

FLASK_ADMIN_FLUID_LAYOUT = True

FLASK_ADMIN_TILE_LAYER_URL = "http://tile.openstreetmap.org/{z}/{x}/{y}.png"
FLASK_ADMIN_TILE_LAYER_ATTRIBUTION = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
