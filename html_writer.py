import os

def save_blog_to_file(title, content):
    os.makedirs("blogs", exist_ok=True)
    filename = "blogs/" + title.lower().replace(" ", "_") + ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"<h1>{title}</h1>\n<p>{content}</p>")
    print(f"Blog saved: {filename}")
