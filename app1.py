from flask import Flask,jsonify

app = Flask(__name__)

Movies=[
    {"id":1,"name":"Dhurandar","category":"action"},
    {"id":2,"name":"Saiyaraa","category":"Romance"},
    {"id":3,"name":"Dangal","category":"Motivational"},
    {"id":4,"name":"MsDhoni","category":"action"},
    {"id":5,"name":"Mirror","category":"action"},
    
]

@app.route("/Movies",methods=["GET"])
def get_by_all_Movies():
    return jsonify(Movies)


@app.route("/Movies/<int:id>",methods=["GET"])
def get_by_id(id):
    for Movie in Movies:
        if Movie["id"]==id:
            return jsonify(Movie)
    return jsonify({"msg":"Movie are not found"})

@app.route("/Movies/<string:name>",methods=["GET"])
def get_by_name(name):
    for Movie in Movies:
            if Movie["name"]==name:
                return jsonify(Movie)
    return jsonify({"msg":"Movie are not found"})

@app.route("/Movies/category/<string:category>",methods=["GET"])
def get_by_category(category):
    r=[]
    for Movie in Movies:
            if Movie["category"]==category:
                r.append(Movie)
                print(r)
            return jsonify(r)    
             
    
if __name__=='__main__':
    app.run(debug=True)