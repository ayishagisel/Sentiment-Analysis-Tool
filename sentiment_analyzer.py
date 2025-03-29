from transformers import pipeline
import streamlit as st

class SentimentAnalyzer:
    def __init__(self):
        """Initialize the sentiment analyzer with a pre-trained model."""
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    
    def analyze_text(self, text: str) -> dict:
        """
        Analyze the sentiment of the given text.
        
        Args:
            text (str): The text to analyze
            
        Returns:
            dict: Dictionary containing the sentiment label and confidence score
        """
        result = self.analyzer(text)[0]
        return {
            "sentiment": result["label"],
            "confidence": round(result["score"] * 100, 2)
        }

def main():
    """Main function to run the sentiment analyzer."""
    # Initialize the analyzer
    analyzer = SentimentAnalyzer()
    
    # Streamlit interface
    st.title("Sentiment Analysis Tool")
    st.write("Enter text below to analyze its sentiment:")
    
    # Text input
    user_input = st.text_area("Input Text", "")
    
    if st.button("Analyze Sentiment"):
        if user_input:
            # Analyze sentiment
            result = analyzer.analyze_text(user_input)
            
            # Display results
            st.subheader("Analysis Results:")
            sentiment_color = "green" if result["sentiment"] == "POSITIVE" else "red" if result["sentiment"] == "NEGATIVE" else "gray"
            st.markdown(f"**Sentiment:** <span style='color:{sentiment_color}'>{result['sentiment']}</span>", unsafe_allow_html=True)
            st.write(f"**Confidence:** {result['confidence']}%")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main() 