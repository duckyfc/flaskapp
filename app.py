from flask import Flask, render_template, request

nameslist = []

app = Flask(__name__)
username = "123"
@app.route("/")
def home():
    return render_template("home.html") 




@app.route("/" + username)   
def username():
    return "Welcome" + username





@app.route("/about")   
def about():
    return render_template("about.html")



@app.route("/form")   
def form():

    name = request.args.get("name")
    nameslist.append(name)
    return render_template("page.html", name = name, nameslist = nameslist)



app.run()

