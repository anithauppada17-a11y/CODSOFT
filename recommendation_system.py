import pandas as pd
movies = {
    'Movie': ['Inception', 'Titanic', 'Avengers', 'The Notebook', 'Joker', 'Interstellar'],
    'Genre': ['Sci-Fi', 'Romance', 'Action', 'Romance', 'Drama', 'Sci-Fi']
}
df = pd.DataFrame(movies)
print("All Movies Available:")
print(df)
print("\n")
user_genre = input("Enter your favorite genre: ")
recommended = df[df['Genre'] == user_genre]
print(f"\nMovies we recommend for {user_genre}:")
if recommended.empty:
    print("Sorry, no movies found for that genre.")
else:
    print(recommended)