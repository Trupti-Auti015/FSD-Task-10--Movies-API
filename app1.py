from flask import Flask,jsonify

app = Flask(__name__)

Movies=[
    {"id":101,"Name":"Dhurandar","Category":"Action"},
    {"id":102,"Name":"Mirror","Category":"Action"},
    {"id":103,"Name":"Cocktail","Category":"Romantic"},
    {"id":104,"Name":"Saiyaraa","Category":"Romantic"},
    {"id":105,"Name":"Mirzapur","Category":"Action"},
    
]

@app.route("/Movies",methods=["GET"])
def get_by_all_Movies():
    return jsonify(Movies)


@app.route("/Movies/<int:id>",methods=["GET"])
def get_by_id(id):
    for Movie in Movies:
        if Movie["id"]==id:
            return jsonify(Movie)
    return jsonify({"msg":"Movie are not found"}),404

@app.route("/Movies/Name/<string:name>",methods=["GET"])
def get_by_name(name):
    for Movie in Movies:
            if Movie["Name"]==name:
                return jsonify(Movie)
    return jsonify({"msg":"Movie are not found"}),404

@app.route("/Movies/Category/<string:Category>",methods=["GET"])
def get_by_category(Category):
    r=[]
    for Movie in Movies:
            if Movie["Category"]==Category:
                r.append(Movie)
                print(r)
    return jsonify(r)    
             
    
if __name__=='__main__':
    app.run(debug=True)