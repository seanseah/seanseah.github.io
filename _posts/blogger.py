import re
import os

for file in os.listdir("_posts"):
    if file.endswith(".md"):
        
        with open('_posts/' + file, 'r') as content_file:
            content = content_file.read()
        modified_1 = re.sub('<[^>]*>', '', content)
        modified_2 = re.sub('s1600-h', 's1600', modified_1)
        output = re.sub('\[\]', '![]', modified_2)
        with open('_posts/' + file, 'w') as output_file:
            output_file.write(output)
            
    elif file.endswith(".html"):
        os.remove ("_posts/" + file)