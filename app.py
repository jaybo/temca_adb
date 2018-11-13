
from __future__ import print_function    
from __future__ import division  

from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = r"mongodb://localhost:27017/Z100"
mongo = PyMongo(app)

databases = {
    'Z100': mongo.cx['Z100'],
    'Z101': mongo.cx['Z101'],
}


@app.route("/")
def home_page():
    data = mongo.db.tar.find_one({'metadata.grid' : {'$eq': '5000'}})
    # return render_template("index.html",
    #     online_users=online_users)
    return "foo" + str(len(data))


@app.route("/<database>/barcode/<grid>")
def barcode(database, grid):
    return 'foo'
    mydb = databases[database]
    data = mydb.tar.find_one({'metadata.grid' : {'$eq': grid}})
    print(database + str(len(data)))
    # print(data)
    return 'database: {}, grid: {}, len: {}'.format(database, grid, len(data))

if __name__ == "__main__":
    app.run(debug=True)