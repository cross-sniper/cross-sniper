import markdown
import os

# HTML template
html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>cross's webpage</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    {{content}}
</body>
</html>
"""


# Function to read file
def read_file(file):
    with open(file, "r") as f:
        return f.read()


# Function to convert Markdown to HTML
def markdown_to_html(markdown_content):
    return markdown.markdown(markdown_content)


# Generate HTML content from Markdown files
def generate_html_from_markdown(directory):
    html_content = ""
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            markdown_content = read_file(os.path.join(directory, filename))
            html_content += f"<details {'open' if filename == 'README.md' else ''}>\n\t<summary>{filename}</summary>\n{markdown_to_html(markdown_content)}\n</details>"
    return html_content


# Generate final HTML by replacing content placeholder in the template
final_html = html_template.replace("{{content}}", generate_html_from_markdown("."))

# Write the final HTML content to a file
with open("index.html", "w") as output_file:
    output_file.write(final_html)
