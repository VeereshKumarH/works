from app.app import create_app
# import sys
# import os

# # Add the parent directory to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Flask Project')))
if __name__=='__main__':
    app = create_app()
    app.run(debug=True)