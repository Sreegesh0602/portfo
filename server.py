
from flask import Flask,render_template,request,redirect
import csv

app=Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Welcome setting up server succesffully created\nEnjoy and celebrate"



# render template is here used to take the html and display it
# route is used to give the url name 
@app.route("/")
def hello_wmy_home():
    return render_template("index.html")



# @app.route("/works.html")
# def Works():
#     return render_template("works.html")


# @app.route("/about.html")
# def about():
#     return  render_template("about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

#BEST WAY TO DO THE ABOVE THINGS

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
     with open("web_development\database.txt",mode="a") as database:
         
         email = data['email']
         subject= data['subject']
         message= data['message']
         file=database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
     with open("web_development\database2.csv",mode="a",newline="") as database2:
         
         email = data['email']
         subject= data['subject']
         message= data['message']
         csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
         csv_writer.writerow([email,subject,message])



@app.route("/submit_form",methods=["POST","GET"])
def submit_forms():
    if request.method=="POST":
        data=request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect("/thankyou.html") 
    else:
        return "something went wrong.Try again later."




