import os

def update_readme():
    is_dark_mode = os.environ.get('GITHUB_COLOR_SCHEME') == 'dark'
    
    logo_url = '![Logo](https://github.com/AryanVBW/Private-Ai/releases/download/I1/Bglight.png)'
    if is_dark_mode:
        logo_url = '![Logo](https://github.com/AryanVBW/Private-Ai/releases/download/I1/Bgdark.png)'

    with open('README.md', 'r') as readme_file:
        readme_content = readme_file.read()

    updated_content = readme_content.replace('![Logo]', logo_url)

    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_content)

if __name__ == "__main__":
    update_readme()
