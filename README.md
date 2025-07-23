# SEO-Blog-Post
This project is an end-to-end automation pipeline for creating short SEO-optimized blog posts using AI. It scrapes trending products, extracts relevant keywords, generates content using OpenAI GPT models, and visualizes insights — all in one tool.

---

Features

1. Scrapes or loads trending product data (mocked sample of 10 products)  
2. Automatically generates SEO keywords for each product  
3. Generates 150–200 word blog posts using OpenAI  
4. Saves each blog as an `.html` file for preview or publishing  
5. Visualizes blog lengths, keyword usage, product categories  
6. Fully modular codebase (for easy reuse and deployment)

---

Folder Structure
seo-blog-generator/
├── main.py # Master script to run the full pipeline
├── sample_products.py # Provides sample or scraped product data
├── keyword_extractor.py # SEO keyword extraction logic
├── blog_generator.py # AI blog post generation via OpenAI
├── html_writer.py # Saves blog posts as HTML
├── visualizations.py # Word cloud, bar chart, pie chart, line graph
├── blogs/ # Folder where all blog HTML files are saved
├── requirements.txt # List of dependencies
└── README.md # Project overview and instructions

pip install -r requirements.txt

