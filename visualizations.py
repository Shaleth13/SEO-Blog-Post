import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from keyword_extractor import get_keywords_for_product

def generate_all_charts(products):
    # Word Cloud
    all_keywords = []
    for p in products:
        all_keywords += get_keywords_for_product(p["title"])
    text = " ".join(all_keywords)
    wordcloud = WordCloud(width=800, height=400, background_color="black").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("SEO Keyword Word Cloud")
    plt.show()

    # Blog Length Bar Chart
    titles = []
    word_counts = []
    for p in products:
        titles.append(p["title"][:25] + "...")
        word_counts.append(len(p["title"].split()) + 150)
    plt.figure(figsize=(12, 5))
    plt.barh(titles, word_counts, color='skyblue')
    plt.xlabel("Word Count")
    plt.title("📏 Blog Length per Product")
    plt.tight_layout()
    plt.show()

    # Product Type Pie Chart
    categories = {"audio": 0, "home": 0, "fitness": 0, "office": 0, "misc": 0}
    for p in products:
        t = p["title"].lower()
        if "earbud" in t or "headphone" in t:
            categories["audio"] += 1
        elif "tv" in t or "purifier" in t:
            categories["home"] += 1
        elif "chair" in t:
            categories["office"] += 1
        elif "band" in t or "fitness" in t:
            categories["fitness"] += 1
        else:
            categories["misc"] += 1
    plt.figure(figsize=(6,6))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', colors=plt.cm.Set3.colors)
    plt.title("Product Type Distribution")
    plt.show()

    # Cumulative Word Count Line Graph
    cum_lengths = np.cumsum([len(p["title"].split()) + 150 for p in products])
    plt.plot(range(1, len(products)+1), cum_lengths, marker='o', linestyle='--', color='green')
    plt.title("Cumulative Word Count Over Posts")
    plt.xlabel("Post Number")
    plt.ylabel("Total Words Written")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
