import flask
import database

app = flask.Flask("__main__")

@app.route("/listings"
    ,methods=["GET"])
def get_listings():
    try:
        min_price = flask.request.args.get('min_price')
        max_price = flask.request.args.get('max_price')
        min_bed = flask.request.args.get('min_bed')
        max_bed = flask.request.args.get('max_bed')
        min_bath = flask.request.args.get('min_bath')
        max_bath = flask.request.args.get('max_bath')

        response = {}
        response["type"] = "FeatureCollection"
        response["features"] = []
        for row in database.query(min_price,max_price,min_bed,max_bed,min_bath,max_bath):
            record = {}
            record["type"] = "Feature"
            record["geometry"] = {"type": "Point", "coordinates": [float(row['lng']), float(row['lat'])]}
            record["properties"] = {}
            record["properties"]["id"] = row["id"]
            record["properties"]["price"] = int(row["price"])
            record["properties"]["street"] = row["street"]
            record["properties"]["bedrooms"] = int(row["bedrooms"])
            record["properties"]["bathrooms"] = int(row["bathrooms"])
            record["properties"]["sq_ft"] = int(row["sq_ft"])
            response["features"].append(record)

        return flask.jsonify(response)
    except:
        flask.Abort(500)
