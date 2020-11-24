# Introduction

The purpose of the package is to help you to visualize the chat messages from a Telegram Chat Group. It is still in development and the features are not extensive. As of now, there are 4 main features in this package (with hopes of more being added)

# Installation

```python
pip install TeleVisuals
```

# Usage

```python
from TeleVisuals import TeleVisuals as tv
```

# Functions

### Clean Data

```python
tv.chat_clean(json_file_path)
```

This function allows you to clean the json export from your telegram chat. The output is a cleaned pandas dataframe with your messages organised by "from", "time", and "messages". 

### Visualise most commonly used words and custom words

```python
tv.common_word(dataframe, no_of_words)
tv.custom_words(dataframe, list_of_words)
```

These functions allow you to visualise words used in your chat. The `common_word` function will allow you to select how many words you want to visualise while the `custom_words` function will allow you to input a list of words that you want to visualise. 

### Visualise user replies and user responses

```python
tv.user_talk(dataframe)
tv.user_replies(dataframe)
```

These functions allow you to visualise the number of times each user spoke and the number of times each user responded to another user. Good to see who is the most talkative one amongst your friends.

# Dependencies 

[Pandas](https://github.com/pandas-dev/pandas): Self-explanatory (who doesn't need pandas?)

[plotly.express](https://github.com/plotly/plotly_express): To enable the visualisations

[json](https://github.com/python/cpython/tree/master/Lib/json): To parse the json file from Telegram chat export