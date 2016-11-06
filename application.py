from flask import Blueprint, Flask
from models import Puppy
from schema import puppy_schema, puppies_schema
from utils import jsonapi


# Create a blueprint for puppy CRUD actions
puppies_v1 = Blueprint('puppies_v1', __name__)


@puppies_v1.route("/puppies")
def get_all_puppies():
    puppies = Puppy.query.all()
    data, _ = puppy_schema.dump(puppies)
    return jsonapi(data)


def create_application():
    app = Flask('kiosk_backend')
    app.register_blueprint(puppies_v1)
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///sqlalchemy_example.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True
    )

    # keep application-specific state separate from SQLALchemy extension object
    from models import db
    db.init_app(app)

    return app


if __name__ == '__main__':
    application = create_application()
    application.run(debug=True, host='0.0.0.0')
