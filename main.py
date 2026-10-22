
# AI Journal Recommendation System

print("=" * 45)
print("     AI JOURNAL RECOMMENDATION SYSTEM")
print("=" * 45)

# Journal dataset
journals = [
    {
        "name": "International Journal of Artificial Intelligence",
        "field": "artificial intelligence",
        "keywords": ["artificial intelligence", "robotics", "expert systems"]
    },
    {
        "name": "Journal of Machine Learning Research",
        "field": "machine learning",
        "keywords": ["machine learning", "deep learning", "reinforcement learning"]
    },
    {
        "name": "Expert Systems with Applications",
        "field": "artificial intelligence",
        "keywords": ["expert systems", "artificial intelligence", "decision support"]
    },
    {
        "name": "Applied Soft Computing",
        "field": "machine learning",
        "keywords": ["machine learning", "optimization", "neural networks"]
    },
    {
        "name": "Knowledge-Based Systems",
        "field": "data mining",
        "keywords": ["data mining", "knowledge systems", "text mining"]
    },
    {
        "name": "Information Sciences",
        "field": "data mining",
        "keywords": ["data mining", "data analysis", "machine learning"]
    },
    {
        "name": "Engineering Applications of Artificial Intelligence",
        "field": "artificial intelligence",
        "keywords": ["artificial intelligence", "robotics", "automation"]
    },
    {
        "name": "Neurocomputing",
        "field": "machine learning",
        "keywords": ["neural networks", "deep learning", "machine learning"]
    },
    {
        "name": "Pattern Recognition",
        "field": "machine learning",
        "keywords": ["pattern recognition", "computer vision", "image processing"]
    },
    {
        "name": "Artificial Intelligence Review",
        "field": "artificial intelligence",
        "keywords": ["artificial intelligence", "deep learning", "natural language processing"]
    }
]

# Related topic mapping
related_topics = {
    "deep learning": "machine learning",
    "neural networks": "machine learning",
    "computer vision": "machine learning",
    "data mining": "data mining",
    "natural language processing": "artificial intelligence",
    "machine learning": "machine learning",
    "artificial intelligence": "artificial intelligence",
    "robotics": "artificial intelligence",
    "expert systems": "artificial intelligence",
    "predictive analytics": "data mining",
    "pattern recognition": "machine learning",
    "image processing": "machine learning",
    "text mining": "data mining",
    "big data": "data mining",
    "reinforcement learning": "machine learning",
    "quantum computing": "artificial intelligence"
}

# Keep the program running until the user exits
while True:
    print("\nAvailable options:")
    print("1. Recommend journals")
    print("2. View all journals")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        topic = input("\nEnter your research topic: ").strip().lower()

        if topic == "":
            print("Error: Research topic cannot be empty.")
            continue

        # Find the matching field
        matching_field = related_topics.get(topic, topic)

        print("\nResearch Paper Topic:", topic)
        print("Topic used for matching:", matching_field)

        # Calculate keyword relevance scores
        recommendations = []

        for journal in journals:
            score = 0

            # Give points when the topic matches a journal keyword
            for keyword in journal["keywords"]:
                if keyword in topic or topic in keyword:
                    score = score + 2

            # Give an additional point for a matching field
            if journal["field"] == matching_field:
                score = score + 1

            # Save journals with a positive score
            if score > 0:
                recommendations.append({
                    "name": journal["name"],
                    "score": score
                })

        # Sort recommendations by score, highest first
        recommendations.sort(
            key=lambda journal: journal["score"],
            reverse=True
        )

        print("\nRecommended Journals:")

        if len(recommendations) == 0:
            print("No matching journals found.")
            print("Try a different or more specific research topic.")

        else:
            count = 0

            for journal in recommendations:
                count = count + 1
                print(
                    str(count) + ". " + journal["name"]
                    + " (Relevance score: "
                    + str(journal["score"]) + ")"
                )

            print("\nTotal recommendations:", count)

        print("-" * 40)

        print("Search completed for topic:", topic)
        print("Recommendations generated:", len(recommendations))

        if len(recommendations) >= 5:
            print("Result Status: Many recommendations")
        elif len(recommendations) >= 3:
            print("Result Status: Good recommendations")
        elif len(recommendations) >= 1:
            print("Result Status: Few recommendations")
        else:
            print("Result Status: No recommendations")

        print("-" * 40)

    elif choice == "2":
        print("\nAvailable Journals:")

        for journal in journals:
            print("-", journal["name"])

        print("\nTotal journals:", len(journals))

    elif choice == "3":
        print("\nThank you for using the AI Journal Recommendation System!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
