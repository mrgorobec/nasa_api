### Status


# TestRepo
**It's NASA API images tests.**

Run Tests local:     
* Install git:
    > brew install git
    
* Next step - install python:
    > brew install python 
    
* Install python virtualenv: 
    > sudo pip install virtualenv
    
* Create virtual environment for mes-backend-automation:
    > virtualenv env

* Activate virtual environment:
    > source env/bin/activate
    
* Clone GitHubAPI repository with ssh ( need configure two factor authorisation and add ssh public key to git hub repository) :
    > git clone https://github.com/nashiluduvsudu/nasa_api.git
    
* Navigate to project folder and install requirements :
    > pip install -r requirements.txt
    
* Run PyTest tests :
    > py.test -v py_test/




