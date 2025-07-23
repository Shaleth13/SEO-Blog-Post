from openai import OpenAI

client = OpenAI(api_key="sk-your-openai-key")  # Replace this securely

def generate_blog_post(product_title, keywords, product_link):
    prompt = f"""
Write a 150-200 word blog post about the product "{product_title}". Use these SEO keywords naturally: {", ".join(keywords)}.
Mention its benefits and add a call-to-action. Link: {product_link}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content
