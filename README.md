<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Clustify: Music Explorer Powered by Clustering

Final project for the Building AI course.

## Summary

Clustify is my first hands-on experiment with AI, developed as part of my learning journey in machine learning. It explores clustering algorithms, particularly K-Means, which wasn’t covered in the course, to group songs based on features like energy, tempo, and danceability. The goal is to help users discover similar tracks and auto-generate personalized playlists based on musical "vibe." It’s a work-in-progress, but a fun way to learn and experiment.


## Background

Most music recommendation systems rely heavily on user behavior, which can reinforce filter bubbles and limit discovery. This project, Clustify, offers an alternative approach based solely on the acoustic properties of songs, encouraging unexpected discoveries and broader musical exploration.

This idea is part of a hands-on AI course exercise. I find interesting the idea of combining music and machine learning to explore new creative possibilities.

## How is it used?

1. Upload a `.csv` file containing song features (e.g., danceability, energy, tempo).
2. Clustify performs clustering using K-Means and displays the results visually.
3. The user explores the resulting clusters to discover similar songs and potential playlist groupings.


## Data sources and AI methods

* Dataset: [Ultimate Spotify Tracks DB – Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
* Libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
* Techniques:
  * Data normalization
  * K-Means clustering
  * Silhouette score for cluster evaluation
  * Elbow method for selecting optimal number of clusters

## Challenges

* Playlist quality may vary depending on feature selection and normalization.
* External factors like lyrics or context aren’t taken into account (yet!).
* K-Means assumes spherical clusters, which may not always reflect the true structure of musical data.

## What next?

* Add a simple UI (maybe with Streamlit) so users can upload their own data and generate playlists with just one click.
* Connect to the Spotify API to fetch music data directly—like audio previews, album covers, or track features.
* Add more features and try to classify songs into emotional categories to generate playlists based on mood — like relaxation, euphoria, or nostalgia.


## Acknowledgments

* [Spotify clustering tutorial – DataCamp](https://www.datacamp.com/tutorial/k-means-clustering-python)
* Dataset: [Kaggle - Ultimate Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
* Building AI course – University of Helsinki & Reaktor
* Special thanks to [Rocío](https://github.com/romodb), my fellow student in a Big Data specialization course, for inspiring me to use the Spotify dataset and introducing me to Streamlit, which I plan to explore in future versions of this project.


