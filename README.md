# sentAnalysis

A Python script that provides sentimental analysis of provided text content.

This was used to analyse qualitative data from think-aloud studies in research for usability evaluations of systems.

## To Run:

- Firstly, ensure you have Python installed. The code should work with Python 3.6 and above.

- You need to have the vaderSentiment library installed. You can install it using pip: `pip install vaderSentiment`

- The `typing` module is included in Python 3.5 and above, so you don't need to install it separately if you're using a modern Python version.

- To use the script, save your text data in a file named input.txt in the same directory as the script. The script will read the file and analyse the sentiment of the text.

- Then execute the script with `python SentAnalysis.py`

## Example Usage

Command line output from the given example text:

> Text: The user interface of Google is intuitive and user-friendly, offering a seamless and efficient experience for both new and seasoned users. The search engine's clean design and uncluttered layout allow for effortless navigation, while the clearly labeled options and minimalistic approach keep the focus on what's important: the search results. Features like Google Voice Search and auto-complete enhance usability and make searching fast and convenient. Google's thoughtful UI choices make it a top choice for anyone looking for a straightforward and efficient search experience.

`Sentiment: Positive, Compound Score: 0.9559`