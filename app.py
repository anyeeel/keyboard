from flask import Flask, render_template, request, redirect, abort
from models import db, Keebs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keyboards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True  # Enable debug mode
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        kbname = request.form['kbname']
        size = request.form['size']
        keycaps = request.form['keycaps']
        switches = request.form['switches']
        stabilizers = request.form['stabilizers']
        case = request.form['case']
        lights = request.form['lights']

        keyboard = Keebs(
            kbname=kbname,
            size=size,
            keycaps=keycaps,
            switches=switches,
            stabilizers=stabilizers,
            case=case,
            lights=lights
        )
        db.session.add(keyboard)
        db.session.commit()
        return redirect('/')

@app.route('/', methods=['GET'])
def RetrieveList():
    keyboards = Keebs.query.all()
    return render_template('index.html', keyboards=keyboards)

@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    keyboard = Keebs.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(keyboard)
        db.session.commit()
        return redirect('/')
    return render_template('delete.html', keyboard=keyboard)

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    keyboard = Keebs.query.get_or_404(id)

    if request.method == 'POST':
        keyboard.kbname = request.form['kbname']
        keyboard.size = request.form['size']
        keyboard.keycaps = request.form['keycaps']
        keyboard.switches = request.form['switches']
        keyboard.stabilizers = request.form['stabilizers']
        keyboard.case = request.form['case']
        keyboard.lights = request.form['lights']

        db.session.commit()
        return redirect('/')
    
    return render_template('update.html', keyboard=keyboard)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
