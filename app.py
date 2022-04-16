from flask import Flask , request
from flask.templating import render_template
from backend import search,search_recom
app = Flask(__name__)

@app.route("/")
def loadd():
    if len(request.args)==0:
        return render_template("movie.html",images=[])
    else:
        name = request.args.get('name')
        toSo = request.args.get('sort').lower()
        toRec = request.args.get('rec').lower()
        com = request.args.get('comedy')
        acti = request.args.get('action')

        if toRec == "yes":
            return render_template("movie.html",images=search_recom(name,com,acti))
        elif toSo == "yes":
            return render_template("movie.html",images=search(name,"True"))
        else:
            return render_template("movie.html",images =search(name,"False"))


if __name__ == "__main__":
    app.run(debug=True)
