from flask import Flask
from exts import db
import config
from flask import __version__

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def hello_world():
    return __version__


if __name__ == '__main__':
    app.run()
