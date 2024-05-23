from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Keebs(db.Model):
    __tablename__ = "keyboards"
    id = db.Column(db.Integer, primary_key=True)
    kbname = db.Column(db.String(255))
    size = db.Column(db.String(50))
    keycaps = db.Column(db.String(255))
    switches = db.Column(db.String(255))
    stabilizers = db.Column(db.String(255))
    case = db.Column(db.String(255))
    lights = db.Column(db.String())

    def __init__(self, kbname, size, keycaps, switches, stabilizers, case, lights):
        self.kbname = kbname
        self.size = size
        self.keycaps = keycaps
        self.switches = switches
        self.stabilizers = stabilizers
        self.case = case
        self.lights = lights

    def __repr__(self):
        return f"<Keebs {self.kbname}:{self.size}>"
