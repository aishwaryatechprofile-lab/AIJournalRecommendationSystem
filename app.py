
import streamlit as st

st.set_page_config(
    page_title="AI Journal Finder",
    page_icon="📚",
    layout="wide"
)

# Sidebar
st.sidebar.title("📚 Journal Finder")
st.sidebar.write("Your research companion")
st.sidebar.divider()

st.sidebar.info(
    "Enter your research topic to discover "
    "potentially relevant academic journals."
)

st.sidebar.caption("AI Journal Recommendation System")


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
        "keywords": [
            "artificial intelligence",
            "deep learning",
            "natural language processing"
        ]
    }
]


# Related research topics
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


# Website heading
st.title("📚 AI Journal Recommendation System")
st.write("Find journals related to your research topic.")
st.divider()


# Research topic input
topic = st.text_input(
    "Enter your research topic",
    placeholder="Example: machine learning"
).strip().lower()


# Search button
if st.button("Find Journals", type="primary"):

    if not topic:
        st.warning("Please enter a research topic.")

    else:
        matching_field = related_topics.get(topic, topic)
        recommendations = []

        # Calculate journal relevance scores
        for journal in journals:
            score = 0

            for keyword in journal["keywords"]:
                if keyword in topic or topic in keyword:
                    score += 2

            if journal["field"] == matching_field:
                score += 1

            if score > 0:
                recommendations.append({
                    "name": journal["name"],
                    "field": journal["field"],
                    "score": score
                })

        # Sort journals by relevance score
        recommendations.sort(
            key=lambda journal: journal["score"],
            reverse=True
        )

        # Search summary
        st.subheader("🔎 Search Results")

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"**Research topic**\n\n{topic}")

        with col2:
            st.info(
                f"**Matching field**\n\n{matching_field.title()}"
            )

        st.metric(
            label="Total Recommendations",
            value=len(recommendations)
        )

        # Display recommendations only once
        if recommendations:
            st.subheader("📚 Recommended Journals")

            for number, journal in enumerate(
                recommendations, start=1
            ):
                with st.container(border=True):
                    st.markdown(
                        f"### {number}. {journal['name']}"
                    )

                    st.caption(
                        f"Research field: {journal['field'].title()}"
                    )

                    st.progress(
                        min(journal["score"] / 5, 1.0)
                    )

                    st.write(
                        f"**Relevance score:** {journal['score']}"
                    )

            # Recommendation summary
            if len(recommendations) >= 5:
                st.success("Many recommendations found!")
            elif len(recommendations) >= 3:
                st.success("Good recommendations found!")
            else:
                st.info("A few recommendations found.")

        else:
            st.warning("No matching journals found.")
            st.info("Try another research topic.")


# View all available journals
with st.expander("View all available journals"):
    for journal in journals:
        st.write(f"- {journal['name']}")
