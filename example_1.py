from textblob import TextBlob

def calculate_polarity(text):
    return TextBlob(text).sentiment.polarity

def convert_polarity_to_score(polarity):
    return 100 - ((polarity + 1) / 2 * 100)

def check_red_flags(text, red_flags):
    return any(red_flag in text for red_flag in red_flags)

def calculate_score(text, red_flags):
    polarity = calculate_polarity(text)
    score = convert_polarity_to_score(polarity)
    if check_red_flags(text, red_flags):
        score = 100
    return score

red_flags = ["I'm always late", "I hate teamwork", "I don't respect deadlines"]
text = "I think I'm always late and I don't respect deadlines"
score = calculate_score(text, red_flags)
print(score)