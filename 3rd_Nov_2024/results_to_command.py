from helper_func import *
from datetime import datetime
import pandas as pd

df = pd.DataFrame(columns=['title', 'content', 'solution', 'created_at', 'status'])


count = 0
values  = ''

no_emoji_data = remove_emojis_from_json("3rd_Nov_2024\\results.json")
messages = no_emoji_data["messages"]

for message in messages:
    
    id = message["id"]
    type = message["type"]
    print(id)
    if type == "message" :
        from_id = message["from_id"]
        if from_id == "user5723398788":
            id = message["id"]
            date = datetime.fromisoformat(message["date"]).strftime('%Y-%m-%d %H:%M:%S')
            date_unixtime = message["date_unixtime"]
            ffrom = message["from"] 
            content = ""
            if not isinstance(message['text'], list):
                content = message['text']
            else:
                text = (message['text'])
                content = escape_special_characters(convert_to_html(message['text']))
            
            if isinstance(text, str):
                title = text
            elif isinstance(text, object):
                title = get_first_bold_text(text).replace(":", "")
            else:
                print("text is neither a string nor an object.")
            
            solution = "<p>Đã xử lý</p>"
            created_at = date
            status = "done"
            print("--------------------------------")
        new_row = {"title": title, "content": content, "solution":"<p>Đã xử lý</p>", "created_at": created_at, "status": "done"}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

df['created_at'] = pd.to_datetime(df['created_at'])
pd.set_option('display.max_colwidth', None)
print(df["content"][0])
df.to_csv(
    'output.csv', 
    index=False,
    sep='\t',
    doublequote=False,
    escapechar='\\'
    )
