import pandas as pd
import sys
import random


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


'''
    PRE: dict that contains the value 'Parent Genres'
    :return a list with non-repeating genres
'''
def get_genres(data):
    genres = set()
    for song_genres in data['Genres']:
        if type(song_genres) == str:
            if ',' in song_genres:
                song_genres = song_genres.split(',')
                for genre in song_genres:
                    genres.add(genre.strip())
            else:
                genres.add(song_genres)
    genres = list(genres)

    return genres


'''
    PRE: A list of genres and a clusters_size > 0
    :return A dict with clusters_size values and
'''
def get_genre_clusters(genres, clusters_size):
    clusters = dict()
    genre_index = 0
    for i in range(clusters_size):
        cluster = set()
        cluster_index = 0
        while genre_index + cluster_index < len(genres) and cluster_index < len(genres) / clusters_size:
            cluster.add(genres[cluster_index + genre_index])
            cluster_index += 1
        clusters[i] = cluster
        genre_index += cluster_index
    return clusters


def sub_playlists(args, clusters_size):
    data = pd.read_csv("data/" + args[0])
    for element in data:
        print(element)
    genres = get_genres(data)
    random.shuffle(genres)
    print(genres)
    print(len(genres))

    genre_clusters = get_genre_clusters(genres,clusters_size)

    for cluster in genre_clusters:
        print(str(cluster) + " " + str(len(genre_clusters[cluster])))
        print(genre_clusters[cluster])








if __name__ == '__main__':
    print_hi('PyCharm')
    sub_playlists(sys.argv[1:], 5)
