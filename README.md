🎬 Movie Recommender System
using Streamlit that recommends movies based on user preferences. It utilizes machine learning and The Movie Database (TMDb) API to suggest movies and display their posters.

📋 Features
Movie Selection: Users can choose a movie from the dropdown.
Recommendations: Get 5 movie recommendations similar to the selected movie.
Posters: Displays movie posters fetched from TMDb.

🛠️ Installation
Install Dependencies
Make sure  Python installed (version 3.9 or above recommended).
Install the required libraries:
pip install -r requirements.txt
Required Libraries
Streamlit: For building the web interface.
Requests: For API calls.
Pandas: For handling movie data.
Pickle: For loading pre-processed data.
Run the Application
streamlit run app.py
The application will open in our default web browser

📂 Files in the Repository
app.py: The main script for running the Streamlit web application.
movie recoommend.ipynb: A Jupyter Notebook implementation for exploring the recommendation process.
movie_dict.pkl: Contains the pre-processed movie dataset.
similarity.pkl: Stores the similarity matrix for efficient movie recommendations.
requirements.txt: Lists the required Python libraries

🛠️ How It Works
Data:
The movie data is pre-processed and stored in movie_dict.pkl.
A similarity matrix (similarity.pkl) is used to find similar movies.

Recommendation:
When a movie is selected, its index is fetched.
The similarity scores are computed to find the top 5 most similar movies.

API Integration:
Posters are fetched using the TMDb API.
✨ Demo
![image](https://github.com/user-attachments/assets/1d9d3e1e-091a-48ee-9a3e-fe1a1749c7c8)


📚 Prerequisites
Python 3.9 or later
A valid API key from The Movie Database (TMDb).

🖊️ Future Improvements
Add more filters for personalized recommendations.
Enhance the UI/UX design.
Support recommendations for multiple languages.
Enable user-authenticated movie lists.
🤝 Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.













