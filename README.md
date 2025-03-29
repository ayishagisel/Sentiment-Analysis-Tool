# Sentiment Analysis Tool

A simple sentiment analysis tool that uses Hugging Face's transformers library to analyze the sentiment of text input. The tool provides both a command-line interface and a Streamlit web interface.

## Features

- Sentiment analysis using DistilBERT model
- Web interface built with Streamlit
- Real-time sentiment analysis with confidence scores
- Color-coded results (green for positive, red for negative)

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To run the Streamlit interface:
```bash
streamlit run sentiment_analyzer.py
```

The web interface will open in your default browser. Enter any text in the input area and click "Analyze Sentiment" to see the results.

## Example Usage

1. Open the application using the command above
2. Enter text such as:
   - "I love this amazing product!" (positive)
   - "This is terrible, I hate it." (negative)
   - "The weather is okay today." (neutral)
3. Click "Analyze Sentiment" to see the results

## Technical Details

- Uses the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face
- Built with Python 3.x
- Dependencies: transformers, torch, streamlit 