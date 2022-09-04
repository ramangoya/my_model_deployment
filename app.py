
from flask  import Flask,render_template,request
import model
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def marks():
    global mk
    mk=1
    if request.method=="POST":
        hrs=request.form["hrs"]
        marks_pred=model.marks_prediction(hrs)
        mk=marks_pred
    return  render_template("index.html",my_marks=mk)

if __name__=="__main__":
    app.run(debug=True)