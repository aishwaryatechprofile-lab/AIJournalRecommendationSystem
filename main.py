# AI Journal Recommendation System

print("AI Journal Recommendation System")

# Research paper details
topic = input("Enter your research topic: ").strip().lower()
paper = {
    "topic": topic
}
# Related research topics


related_topics = {
    "deep learning": "machine learning",
    "neural networks": "machine learning",
    "computer vision": "machine learning",
    "data mining": "data mining",
    "natural language processing": "artificial intelligence"
}

print("Research Paper Topic:", paper["topic"])

# Journal dataset
journals = [
    {
        "name": "International Journal of Artificial Intelligence",
        "field": "Artificial Intelligence",
        "type": "Research Journal"
    },
    {
        "name": "Journal of Machine Learning Research",
        "field": "Machine Learning",
        "type": "Research Journal"
    },
    {
        "name": "Expert Systems with Applications",
        "field": "Artificial Intelligence",
        "type": "Research Journal"
    },
    {
        "name": "Applied Soft Computing",
        "field": "Machine Learning",
        "type": "Research Journal"
    },
    {
        "name": "Knowledge-Based Systems",
        "field": "Data Mining",
        "type": "Research Journal"
    },
    {
        "name": "Information Sciences",
        "field": "Data Mining",
        "type": "Research Journal"
    },
    {
        "name": "Engineering Applications of Artificial Intelligence",
        "field": "Artificial Intelligence",
        "type": "Research Journal"
    },
    {
        "name": "Neurocomputing",
        "field": "Machine Learning",
        "type": "Research Journal"
    },
    {
        "name": "Pattern Recognition",
        "field": "Machine Learning",
        "type": "Research Journal"
    },
    {
        "name": "Artificial Intelligence Review",
        "field": "Artificial Intelligence",
        "type": "Research Journal"
    },

]

# Display all journals
print("\nAvailable Journals:")

for journal in journals:
    print(journal["name"])

# Recommend journals

recommended_topic = related_topics.get(
    paper["topic"], paper["topic"]
)

print("Topic used for matching:", recommended_topic)
print("\nRecommended Journals:")

found = False
count = 0

for journal in journals:
    if recommended_topic == journal["field"].lower():
        print(journal["name"])
        count = count + 1
        found = True

if found == False:
    print("No matching journals found.")
else:
    print("Total recommendations:", count)

print("------------------------------")
print("Search completed for topic:", paper["topic"])
print("Recommendations generated:", count)
print("------------------------------")


# Recommendation result rating
if count >= 5:
    print("Result Status: Many recommendations")
elif count >= 3:
    print("Result Status: Good recommendations")
elif count >= 1:
    print("Result Status: Few recommendations")
else:
    print("Result Status: No recommendations")
