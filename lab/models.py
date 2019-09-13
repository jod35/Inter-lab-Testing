from lab import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.Text())
    name=db.Column(db.Text(),nullable=False)
    accredited=db.Column(db.Boolean(),nullable=False)
    password=db.Column(db.Text(),nullable=False)
    samples = db.relationship('Sample',
      backref= 'lab',
      lazy=True
    )

    def __repr__(self):
        return 'user {}'.format(self.name)



class Sample(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    patient_name=db.Column(db.Text(),nullable=False)
    Sample_type=db.Column(db.Text(),nullable=False)
    med_record_no=db.Column(db.Text(),nullable=False)
    patient_location=db.Column(db.Text(),nullable=False)
    collection_time=db.Column(db.DateTime(),default=datetime.utcnow)
    ordering_lab=db.Column(db.Text(),nullable=False)
    accepted=db.Column(db.Boolean())
    lab_id=db.Column(db.Integer(),db.ForeignKey('user.id'))


    def __repr__(self):
        return 'sample of %s {}  at %d'.format(self.patient_name,self.collection_time)
