from crypt import methods
from flask import Flask, jsonify, request 

app= Flask(__name__)


#Boiler Plate for future Users method 
@app.route('/api/users', methods=['GET'])
def get_users():

    users =[
        {'id':1,'name':'Abe Ansari'},
        
    ]

    return jsonify(users)


@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()

if __name__ == '__main__':
    app.run()


@app.route('/api/Journal',methods=['GET'])
def get_journal():
    print("Journal")
    """
    select Journal entries where user ID = user ID 
    sorted by time 

    jsonify 

    return a list of JSON 
    
    
    """

@app.route('/api/Journal',methods=['POST'])
def create_journal():
    print("Journal")


    """
    create Journal entry in journal table where User id = ....



    """

@app.route('/api/JournalDelete',methods=['POST'])
def delete_journal():
    print ("Journal")
    """
    remove row where journal ID = ID 
    
    ID can be stored in the JSON
    
    
    
    """
"""
Sample Java Script 

fetch('/api/users')
  .then(response => response.json())
  .then(data => {
    // Handle the response data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors
    console.error(error);
  });

// Example of creating a user
const user = { name: 'New User' };
fetch('/api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(user)
})
.then(response => response.json())
.then(data => {
    // Handle the response data
    console.log(data);
})
.catch(error => {
    // Handle any errors
    console.error(error);
});




"""