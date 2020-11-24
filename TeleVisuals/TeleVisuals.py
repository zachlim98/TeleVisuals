import pandas as pd
import json
from pandas.io.json import json_normalize
import plotly.express as px 

def chat_clean(file_path):
    '''Enter the file_path for .json Telegram Chat export'''
    with open(file_path, encoding="utf8") as f:
        d = json.load(f)
    norm_msg = json_normalize(d['messages'])
    msg_df = pd.DataFrame(norm_msg)
    msg_df_filtered = msg_df[msg_df.type=="message"]
    msg_df_filtered = msg_df_filtered[["date","text","from"]]
    msg_df_filtered['text'] = msg_df_filtered['text'].str.replace('[^A-Za-z0-9]+', " ")
    msg_df_filtered = msg_df_filtered.dropna()

    return msg_df_filtered

def common_word(dataframe,word_no):
    '''Visualizes the top X most common words used'''
    common_word = pd.Series(' '.join(dataframe['text']).lower().split()).value_counts()[:int(word_no)]
    common_word = common_word.reset_index().rename(columns={"index":"Word", 0:"Count"})
    fig = px.bar(common_word, x='Word', y='Count')
    
    return fig

def custom_words(dataframe,word_list):
    '''Visualizes a custom list of words'''
    int_word_count = [sum(pd.Series(' '.join(dataframe['text']).lower().split())==i) for i in word_list]

    int_words = pd.DataFrame(
    {"Word" : word_list,
    "Count" : int_word_count}
    )

    fig = px.bar(int_words, x="Word",y="Count",color_discrete_sequence=px.colors.qualitative.G10)

    return fig

def user_talk(dataframe):
    '''Visualizes the number of texts sent by each user'''
    messages_sent = dataframe['from'].value_counts()
    messages_sent = messages_sent.reset_index().rename(columns={"index":"User", "from":"Count"})

    fig2 = px.bar(messages_sent, x='User', y='Count')

    return fig2 

def user_replies(dataframe):
    '''Visualizes the number of user responses to other users'''
    replies = [dataframe.iloc[n,2] + " to " + dataframe.iloc[(n-1),2] for n in range(1,len(dataframe))]
    replies.insert(0,"No Reply")

    dataframe['Replies'] = replies

    replies_to = dataframe['Replies'].value_counts()
    replies_to = replies_to.reset_index().rename(columns={"index":"Replies", "Replies":"Count"})

    fig3 = px.bar(replies_to, x='Replies', y='Count')
    
    return fig3