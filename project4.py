import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_series_data():
    return pd.DataFrame({
        'title': [
            'Breaking Bad', 'Stranger Things', 'Money Heist', 'Dark', 'The Crown',
            'Narcos', 'Peaky Blinders', 'The Witcher', 'House of Cards', 'The Queen’s Gambit'
        ],

        'genre': [
            'Crime Drama  Chemistry Revenge Thriller',
            'Sci-Fi Horror Teens Mystery',
            'Action RebillionThriller Heist',
            'Time Travel Mystery',
            'Historical Drama Royal Politics',
            ' Drug Mafia Biographical Violence',
            'Crime Drama British Family Brotherhood',
            'Fantasy Action Magic Adventure',
            'Political Drama Power Thriller',
            'Drama Chess Feminism'
        ]
    })

def build_similarity_matrix(df):
    vectorizer = TfidfVectorizer()
    genre_matrix = vectorizer.fit_transform(df['genre'])
    return cosine_similarity(genre_matrix)

def recommend_series(series_name, df, similarity_matrix):
    if series_name not in df['title'].values:
        print("❌ Series not found in database.")
        return

    index = df[df['title'] == series_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

    print(f"\n📺 Recommendations similar to '{series_name}':")
    for i in sorted_scores[:3]:
        print(f"- {df.iloc[i[0]]['title']}")


def main():
    df = load_series_data()
    similarity_matrix = build_similarity_matrix(df)
    recommend_series("Stranger Things", df, similarity_matrix)

main()