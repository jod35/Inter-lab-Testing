from lab import app,db
from flask import jsonify,request
from lab.models import User,Sample
import uuid
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/user',methods=['GET'])
def  get_all_users():
    users=User.query.all()
    if not users:
       return jsonify({"message":"No Users"})

    output=[]
    for user in users:
       user_data={}
       user_data['public_id']=user.public_id
       user_data['name']=user.name
       user_data['password']=user.password
       user_data['accredited']=user.accredited
       output.append(user_data)

    return jsonify({"users":output}) 
         


@app.route('/user/<public_id>',methods=['GET'])
def get_a_single_user(public_id):
   user=User.query.filter_by(public_id=public_id).first()
   if not user:
      return jsonify({"message" : "No User Found"})
   user_data={}
   user_data['public_id']=user.public_id
   user_data['name']=user.name
   user_data['password']=user.password
   user_data['accredited']=user.accredited
   return jsonify({"user": user_data}) 
   
          

@app.route('/user', methods=['POST'])
def add_user():
   data= request.get_json()
   hashed_password=generate_password_hash(data['password'],method='sha256')
   name=data['name'], 
   password=hashed_password,
   new_user=User(
     public_id=str(uuid.uuid4()),
     name=name,
     password=hashed_password,
     accredited=False
   ) 
   db.session.add(new_user)
   db.session.commit()
   return jsonify({"message" :"New User Added Successfully"}) 
   
   

@app.route('/user/<public_id>',methods=['PUT'])
def promote_user(public_id):
   user=User.query.filter_by(public_id=public_id).first()
   user.accredited=True
   db.session.commit()
   return jsonify({"message":"User Is Accredited!"})

@app.route('/user/<public_id>',methods=['DELETE'])
def delete_user(public_id):
   user=User.query.filter_by(public_id=public_id).first()
   db.session.delete(user)
   return jsonify({"message":"User Has Been Deleted"})