# Smart Resume Generator

An AI-powered resume generator built with Streamlit and powered by the `gemma:2b` model running on Ollama.

## Project Structure
- `app.py` — Main Streamlit app
- `utils.py` — Helper functions
- `job_scraper.py` — Job data scraping

## How to Run Locally

1. Install Ollama: https://ollama.com

2. Pull the model:

    ollama pull gemma:2b

3. Clone the repository and install dependencies:

Open your terminal or command prompt.

Run these commands one at a time:

    git clone https://github.com/Vanshdudeja27/Smart-Resume-Generator.git
    cd Smart-Resume-Generator
    pip install -r requirements.txt

4. Run the application:
      streamlit run app.py
