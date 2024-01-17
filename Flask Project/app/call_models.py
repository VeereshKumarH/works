from flask import Blueprint, Flask

mask_detector = Blueprint('mask_detector',__name__,url_prefix='/mask_detector/')
iris_detector = Blueprint('iris_detector',__name__,url_prefix='/iris_detector/')
titanic_survivor = Blueprint('titanic_survivor',__name__,url_prefix='/titanic_detector/')

@mask_detector.route('classify/')
def classify():
    return 'mask classifier'

@iris_detector.route('classify/')
def classify():
    return 'iris classifier'

@titanic_survivor.route('classify/')
def classify():
    return 'titanic survivor'

def register_blueprints(app):
    app.register_blueprint(mask_detector)
    app.register_blueprint(iris_detector)
    app.register_blueprint(titanic_survivor)

if __name__=='__main__':
    app = Flask(__name__)
    register_blueprints(app)
    app.run(use_reloader=True,debug=False)