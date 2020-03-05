from application import app

@app.route('/')
def hello():
    return "Return Hello"


@app.route('/contact')
def contact:
    return "Contact us flask template example"


@app.route('/login', methods=['GET','POST'])
def login:
    if request.method == 'POST'
        pass
    else:
        pass
