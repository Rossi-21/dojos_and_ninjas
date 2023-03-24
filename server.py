from flask_app import app
from flask_app.controllers import dojo_controller, ninja_controller #import other controllers with a ,

if __name__=="__main__":       
    app.run(debug=True)    

