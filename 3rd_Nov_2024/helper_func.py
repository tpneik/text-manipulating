import re
import json

def convert_to_html(text_array):
    html_string = ""
    for part in text_array:
        
        if isinstance(part, dict):
            text_data = (part["text"])
            if part['type'] == 'bold':
                html_string += f"<strong>{text_data}</strong>"
            elif part['type'] == 'underline':
                html_string += f"<u>{text_data}</u>"
            elif part['type'] == 'link':
                html_string += f'<a href="http://{text_data}">{text_data}</a>'
                
        elif isinstance(part, str):
            html_string += part.replace('\n', '<br>')  # Convert newlines to <br> tags
    print (html_string)
    return html_string

def escape_special_characters(text):
    if isinstance(text, str):
        text = (text
                    # .replace("\\", "\\\\")  # Escape backslash
                    .replace("'", "\'")  # Escape single quote
                    .replace('"', '\"')  # Escape double quote
                    .replace("\n", "\\n")  # Escape newline
                    .replace("\r", "\\r")  # Escape carriage return
                    .replace("\t", "\\t"))  # Escape tab
    return repr(text)

def get_first_bold_text(data):
    for part in data:
        if isinstance(part, dict) and part.get('type') == 'bold':
            return part['text']
    return None

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # Emoticons
                               u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # Transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # Flags (iOS)
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"  # Enclosed characters
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Function to read, process, and save a cleaned JSON file
def remove_emojis_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Function to recursively remove emojis from JSON content
        def clean_json(obj):
            if isinstance(obj, dict):
                return {key: clean_json(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [clean_json(item) for item in obj]
            elif isinstance(obj, str):
                return remove_emojis(obj)
            else:
                return obj

        cleaned_data = clean_json(data)

        return cleaned_data

    except Exception as e:
        print(f"Error processing the JSON file: {e}")