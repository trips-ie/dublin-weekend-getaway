import json
import random

# Load the destinations and their features from a JSON file
with open('destinations.json') as file:
    destinations = json.load(file)

# Function to suggest a destination based on the given preferences
def suggest_destination(outdoors, pubs, dancing, history, food, art_culture, relaxation, adventure, shopping, nightlife, family_friendly):
    # Create a list of destinations that match the user's preferences
    matches = []
    for name, features in destinations.items():
        if (outdoors == features['outdoors'] and
            pubs == features['pubs'] and
            dancing == features['dancing'] and
            history == features['history'] and
            food == features['food'] and
            art_culture == features['art_culture'] and
            relaxation == features['relaxation'] and
            adventure == features['adventure'] and
            shopping == features['shopping'] and
            nightlife == features['nightlife'] and
            family_friendly == features['family_friendly']):
            matches.append(name)

    # If there are no matches, return None
    if len(matches) == 0:
        return None

    # Otherwise, return a random matching destination
    return random.choice(matches)

# Ask the user for their preferences
print('Answer the following questions to help us suggest a weekend getaway from Dublin.')
outdoors = input('Do you prefer being outdoors (yes/no)? ').lower() == 'yes'
pubs = input('Do you like pubs (yes/no)? ').lower() == 'yes'
dancing = input('Do you like dancing (yes/no)? ').lower() == 'yes'
history = input('Are you interested in history (yes/no)? ').lower() == 'yes'
food = input('Are you a foodie (yes/no)? ').lower() == 'yes'
art_culture = input('Are you interested in art and culture (yes/no)? ').lower() == 'yes'
relaxation = input('Are you looking for a quiet and peaceful place to relax (yes/no)? ').lower() == 'yes'
adventure = input('Are you looking for outdoor activities that provide a thrill (yes/no)? ').lower() == 'yes'
shopping = input('Do you enjoy shopping (yes/no)? ').lower() == 'yes'
nightlife = input('Are you looking for a destination with a vibrant nightlife (yes/no)? ').lower() == 'yes'
family_friendly = input('Are you looking for a family-friendly destination (yes/no)? ').lower() == 'yes'

# Use the function to suggest a destination based on the user's preferences
destination = suggest_destination(outdoors, pubs, dancing, history, food, art_culture, relaxation, adventure, shopping, nightlife, family_friendly)

# Print the suggested destination
if destination is not None:
    print(f"We suggest you to visit {destination} this weekend!")
else:
    print("Sorry, we couldn't find a matching destination for your preferences.")
