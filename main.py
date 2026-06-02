import csv

movies = []

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movies.append(row)

movie_name = input("Enter Movie Name: ")

selected_genre = None

for movie in movies:
    if movie["Movie"].lower() == movie_name.lower():
        selected_genre = movie["Genre"]

if selected_genre:
    print("\nRecommended Movies:")

    for movie in movies:
        if movie["Genre"] == selected_genre and movie["Movie"].lower() != movie_name.lower():
            print(movie["Movie"])

else:
    print("Movie Not Found")