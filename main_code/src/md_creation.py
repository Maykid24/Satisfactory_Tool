import datetime

def create_markdown_template():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define the content of the Markdown file
    content = f"""# Session Notes - {current_date}

## What was done during the session
- 

## What needs to get done on the next session
- 

## Things to research / Design / Need additional info, etc.
- 
"""

    # Define the file name with the current date
    file_name = f"text_files/Session_Notes_{current_date}.md"

    # Write the content to a new Markdown file
    with open(file_name, "w") as file:
        file.write(content)

    print(f"Markdown file '{file_name}' created successfully!")

# Run the function to create the file
create_markdown_template()
