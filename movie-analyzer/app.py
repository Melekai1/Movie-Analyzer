from flask import Flask, render_template, jsonify  # type: ignore[import]
import csv

app = Flask(__name__) 

def load_movie_initial_data():
    movies = []
    with open("moviesHomePage.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(row)
        return movies


def load_all_movie_data():
    movieList = []
    with open("movies.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movieList.append(row)
        return movieList



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/distributor")
def distributor():
    return render_template("distributor.html")


@app.route("/api/movies") 
def get_movies():
    movies = load_movie_initial_data()
    return jsonify(movies)


 @app.route("/api/all_movies")
 def get_all_movies():
    movies = load_all_movie_data()
    return jsonify(movies)



if __name__ == "__main__":
    app.run(debug=True)
    

