from sample_products import get_sample_products
from keyword_extractor import get_keywords_for_product
from blog_generator import generate_blog_post
from html_writer import save_blog_to_file
from visualizations import generate_all_charts

from IPython.core.display import display, HTML
import pandas as pd

products = get_sample_products()
df = pd.DataFrame(products)
print("Products Processed:")
display(df)

for product in products:
    print(f"\n Processing: {product['title']}")
    keywords = get_keywords_for_product(product["title"])
    blog_post = generate_blog_post(product["title"], keywords, product["link"])
    save_blog_to_file(product["title"], blog_post)
    display(HTML(f"<div style='background:#f5f5f5;padding:15px'><h3>{product['title']}</h3><p>{blog_post}</p></div>"))

generate_all_charts(products)
