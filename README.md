# Movie Recommender System

This is a Movie Recommender System built using Streamlit. It recommends movies based on a selected movie and displays the recommendations with their posters, release dates, ratings, genres, and overviews.

## Features

- Select a movie from the dropdown list.
- Get recommendations for similar movies.
- Display movie posters, release dates, ratings, genres, and overviews.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NoteAditya/movie-recommender.git
    cd movie-recommender
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the `data` directory contains the necessary files:
    - `movies_dict.pkl`
    - `similarity.zip` (which contains `similarity.pkl`)

## Usage

1. Run the application:
    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select a movie from the dropdown list and click the "Recommend" button to get movie recommendations.

## File Structure

- `main.py`: The main application file.
- `templates/template.html`: The HTML template for displaying movie recommendations.
- `static/style.css`: The CSS file for styling the HTML template.
- `data/movies_dict.pkl`: The pickle file containing movie data.
- `data/similarity.zip`: The zip file containing the similarity matrix.

## Requirements

- Python 3.8 or higher
- Streamlit 1.42.2
- Other dependencies listed in `requirements.txt`

## Demo

You can get a demo at [www.pac-mrs.streamlit.app](https://www.pac-mrs.streamlit.app)
