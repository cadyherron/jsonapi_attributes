from flask import Flask


def create_application():
    app = Flask('kiosk_backend')
    # keep application-specific state separate from SQLALchemy extension object
    # from models import db
    # db.init_app(app)
    return app


if __name__ == '__main__':
    application = create_application()
    application.run(debug=True, host='0.0.0.0')