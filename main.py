##integrate html with flask
#(jinja2 techniques):i.e you'll have a seperate data source and you can integrate it with html however you wat
#using HTTP verb GET and POST
#building url dynamically
## Variable rules and url building

from flask import Flask,redirect,url_for,render_template,request
app2=Flask(__name__)

@app2.route('/')
def intro():
    return render_template('intro.html')

##building url dynamically(using rules)
@app2.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

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
    return redirect (url_for(result,score=marks)) #redirect is used for making url

#result checker submit html page
@app2.route('/submit',methods=['POST','GET'])
def submit():
    #request will help you to read the posted values
    total_score=0
    if request.method=='POST':
        #'scciene' shd be same as id in html file 
        science = float(request.form['science'])  # Correct
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score=(science+maths+c+datascience)/4
        return redirect(url_for('success',score=total_score))#this function does dynamic url generation
    
    
if __name__== '__main__':
    app2.run(debug=True)


