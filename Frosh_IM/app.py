from flask import Flask, request, render_template 

app = Flask(__name__)


SPORTS = [
    'Football',
    'Badminton',
    'Cricket',
]

# Registering our users
REGISTRANTS = {}

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)

# @app.route('/register', methods=['POST'])
# def register():
#     name = request.form.get('name')
#     sport = request.form.get('sport')
#     if not name or sport not in SPORTS:
#         return render_template('failure.html')
#     return render_template('success.html', name=name, sport=sport)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return render_template('error.html', message='Empty Name Bruv!')
    
    sport = request.form.get('sport')
    if not sport:
        return render_template('error.html', message='Empty Sport Bruv!')
    elif sport not in SPORTS:
        return render_template('error.html', message="Don't be smart Bruv!")
    
    REGISTRANTS[name] = sport
    
    return render_template('success.html')

@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=REGISTRANTS)


if __name__ == '__main__':
    app.run(debug=True)