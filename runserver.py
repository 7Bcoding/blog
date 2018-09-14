from blog2 import app

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)



