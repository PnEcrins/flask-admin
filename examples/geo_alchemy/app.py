from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


from geojson import Feature, FeatureCollection
from geoalchemy2.shape import to_shape


import flask_admin as admin
from geoalchemy2.types import Geometry
from flask_admin.contrib.geoa import ModelView


# Create application
app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("POINT"))


class MultiPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("MULTIPOINT"))


class Polygon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("POLYGON"))


class MultiPolygon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("MULTIPOLYGON"))


class LineString(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("LINESTRING"))


class MultiLineString(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    point = db.Column(Geometry("MULTILINESTRING"))


# Flask views
@app.route("/")
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


# Create admin
admin = admin.Admin(app, name="Example: GeoAlchemy", template_mode="bootstrap4")


class GeomListView(ModelView):
    list_template = "admin/liste_geo.html"
    tile_layer_url = "{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    tile_layer_attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

    def __init__(
        self,
        model,
        session,
        geometry_column,
        name=None,
        category=None,
        endpoint=None,
        url=None,
        static_folder=None,
        menu_class_name=None,
        menu_icon_type=None,
        menu_icon_value=None,
    ):
        self.geometry_column = geometry_column
        super(GeomListView, self).__init__(
            model,
            session,
            name,
            category,
            endpoint,
            url,
            static_folder,
            menu_class_name,
            menu_icon_type,
            menu_icon_value,
        )

    def render(self, template, **kwargs):
        features = []
        for d in kwargs["data"]:
            properties = {}
            for name, label in self.get_list_columns():
                if name != self.geometry_column:
                    properties[name] = self.get_list_value(None, d, name)
                    properties["id"] = self.get_pk_value(d)

            #     print(type(model_attr))
            features.append(
                Feature(
                    geometry=to_shape(getattr(d, self.geometry_column)),
                    properties=properties,
                )
            )
        self._template_args["geojson_data"] = FeatureCollection(features)
        return super(GeomListView, self).render(template, **kwargs)


class PointAdminView(GeomListView, ModelView):
    can_create = True
    can_delete = True
    can_update = True


# Add views
admin.add_view(
    PointAdminView(Point, db.session, geometry_column="point", category="Points")
)
admin.add_view(ModelView(MultiPoint, db.session, category="Points"))
admin.add_view(ModelView(Polygon, db.session, category="Polygons"))
admin.add_view(ModelView(MultiPolygon, db.session, category="Polygons"))
admin.add_view(ModelView(LineString, db.session, category="Lines"))
admin.add_view(ModelView(MultiLineString, db.session, category="Lines"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Start app
    app.run(debug=True)


# TODO : rajouter l'ID a chaque ligne pour faire le lien
