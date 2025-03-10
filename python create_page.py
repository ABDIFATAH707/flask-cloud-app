import os

# Define the folder name
folder_name = "Abdifatah_Page"

# Create the folder
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create the HTML file
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdifatah Soane Ahmed</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="box">
            <h1>Abdifatah Soane Ahmed</h1>
            <h2>Reg/no: 23/07836 (BSD)</h2>
            <p class="quote">"Welcome to a realm where innovation meets elegance, and every pixel tells a story. Let your curiosity be your guide as you explore this digital masterpiece."</p>
        </div>
    </div>
</body>
</html>'''

with open(os.path.join(folder_name, "index.html"), "w") as html_file:
    html_file.write(html_content)

# Create the CSS file
css_content = '''body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.container {
    text-align: center;
    background: url('lamborghini.jpg') no-repeat center center/cover;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    border: 4px double #fff;
}

.box {
    background: rgba(0, 0, 0, 0.7);
    padding: 20px;
    border-radius: 10px;
}

h1 {
    font-size: 3rem;
    margin: 0;
    color: #ffdd57;
    text-shadow: 2px 2px 4px #000;
}

h2 {
    font-size: 2rem;
    margin: 10px 0;
    color: #ffdd57;
    text-shadow: 2px 2px 4px #000;
}

.quote {
    font-size: 1.2rem;
    font-style: italic;
    color: #fff;
    text-shadow: 1px 1px 2px #000;
    margin-top: 20px;
}'''

with open(os.path.join(folder_name, "styles.css"), "w") as css_file:
    css_file.write(css_content)

print(f"Folder '{folder_name}' created successfully with HTML and CSS files.")