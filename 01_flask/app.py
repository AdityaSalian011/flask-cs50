from flask import Flask, render_template, request

app = Flask(__name__)
# tell python to turn this file into a web format and access it's property using the variable/object app


# @app.route('/')
# def index():
#     return 'Hello, world'

# @app.route('/')
# def index():
#     return '<!DOCTYPE><html lang="en"><head><title>Hello World</title></head><body><h1>Hello, world</h1></body></html>'

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def index():
#     if 'name' in request.args:
#         name = request.args['name']
#     else:
#         name = 'world'
#     return render_template('index.html', name=name)

@app.route('/')
def index():
    name = request.args.get('name', 'world')
    return render_template('index.html', name=name)

if __name__=='__main__':
    app.run(debug=True)