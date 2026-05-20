items = [
    {"keyword": "hot", "recommendation": "Summer"},
    {"keyword": "cold", "recommendation": "Winter"},
    {"keyword": "rain", "recommendation": "Autumn"},
    {"keyword": "snow", "recommendation": "Winter"},
    {"keyword": "sunny", "recommendation": "Spring"},
    {"keyword": "wind", "recommendation": "Autumn"},
]

def get_recommendation(user_input):
    user_input = user_input.lower()
    for item in items:
        if item["keyword"] in user_input:
            return item["recommendation"]
    return "No recommendation found"