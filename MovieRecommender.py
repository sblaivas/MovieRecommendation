#Description: Build a movie recommendation engine

#Import the libraries 
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Correcting the filename in the path
genome_scores_path = '/Users/stevenblaivas/Downloads/Movie Dataset/genome-scores.csv'
genome_tags_path = '/Users/stevenblaivas/Downloads/Movie Dataset/genome-tags.csv'
links_path = '/Users/stevenblaivas/Downloads/Movie Dataset/links.csv'
movies_path = '/Users/stevenblaivas/Downloads/Movie Dataset/movies.csv'
ratings_path = '/Users/stevenblaivas/Downloads/Movie Dataset/ratings.csv'
tags_path = '/Users/stevenblaivas/Downloads/Movie Dataset/tags.csv'

#Load the data from the data set
genome_scores_df = pd.read_csv(genome_scores_path)
#movieId: The ID of the movie. 
#tagId: The ID of the tag. 
#relevance: A score between 0 and 1 that represents the relevance of the tag to the movie.

genome_tags_df = pd.read_csv(genome_tags_path)
#tagId: The ID of the tag.
#tag: The text of the tag itself.

links_df = pd.read_csv(links_path)
#movieId: The ID of the movie in the MovieLens dataset.
#imdbId: The corresponding ID of the movie in the IMDb database.
#tmdbId: The corresponding ID of the movie in The Movie Database (TMDB).

movies_df = pd.read_csv(movies_path)
#movieId: The ID of the movie.
#title: The title of the movie, often including the release year.
#genres: A list of genres assigned to the movie, separated by the pipe (|) character.

ratings_df = pd.read_csv(ratings_path)
#userId: The ID of the user who made the rating.
#movieId: The ID of the movie that was rated.
#rating: The rating given to the movie, typically on a scale (e.g., 0.5 to 5 stars).
#timestamp: The time the rating was made.

tags_df = pd.read_csv(tags_path)
#userId: The ID of the user who added the tag to the movie.
#movieId: The ID of the movie to which the tag was added.
#tag: The text of the tag.
#timestamp: The time the tag was added.


#Get the number of rows and columns in each data set
genome_scores_shape = genome_scores_df.shape
genome_tags_shape = genome_tags_df.shape
links_shape = links_df.shape
movies_shape = movies_df.shape
ratings_shape = ratings_df.shape
tags_shape = tags_df.shape


# List of important columns from each DataFrame
# Extract the release year and create a new column combining title and release year in the format "Title (Release Year)"
movies_df['title_with_year'] = movies_df['title'].str.replace(r'(\(\d{4}\))', r'\1')
# Specify the columns of interest to include the newly created 'title_with_year' and 'genres'
columns_of_interest = ['title_with_year', 'genres']


#Check for any null values for the specific columns that we are interested in.
# Check for null values in the 'title_with_year' and 'genres' columns
null_counts = movies_df[['title_with_year', 'genres']].isnull().sum()
# Print the count of null values for each column
print(null_counts)




