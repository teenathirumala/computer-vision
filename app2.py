#building url dynamically
## Variable rules and url building

from flask import Flask,redirect,url_for
app2=Flask(__name__)

@app2.route('/')
def intro():
    return 'hey everyone!!'

##building url dynamically(using rules)
@app2.route('/success/<int:score>')
def success(score):
    return "the person has passed and the marks are "+str(score)


@app2.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks are "+str(score)


@app2.route('/results/<int:marks>')
#result checker
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    # return result
    return redirect (url_for(result,score=marks))

if __name__== '__main__':
    app2.run(debug=True)


