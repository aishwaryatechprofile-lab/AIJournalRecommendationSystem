# 📚 AI Journal Recommendation System

## About the Project
The AI Journal Recommendation System is a Python-based web application that helps users discover potentially relevant academic journals based on their research topics.

Users can enter a research topic and receive journal recommendations ranked using keyword matching and research-field matching.

## Features
- Search journals using a research topic
- Match topics to research fields
- Calculate relevance scores
- Display ranked journal recommendations
- Show the total number of recommendations
- Display a message when no matching journals are found
- View the complete list of available journals
- Interactive website built with Streamlit

## Technologies Used
- Python
- Streamlit

## Project Structure
```text
AIJournalRecommendationSystem/
├── app.py
├── main.py
├── README.md
└── .venv/
```

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install Streamlit:

```bash
python -m pip install streamlit
```

4. Start the website:

```bash
python -m streamlit run app.py
```

5. Open the local URL displayed in the terminal.

## How It Works
1. The user enters a research topic.
2. The system identifies a related research field when available.
3. It compares the topic with journal keywords.
4. It calculates relevance scores.
5. It sorts and displays matching journals.

## Current Limitations
The current version uses predefined journal data and rule-based keyword matching. It does not yet use a trained machine learning model, and relevance scores do not represent verified journal quality.

## Future Improvements
- Add more academic journals and research fields
- Use NLP to understand similar research topics
- Integrate a verified academic journal dataset
- Add journal links and publication details
- Improve recommendation accuracy

---
**Project:** AI Journal Recommendation System
