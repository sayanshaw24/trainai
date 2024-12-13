# trainai
AI for AI - Leveraging LLMs to Create Training Dataset Collections

## About

Data scientists that work on building machine learning models have the imperative task of determining and conglomerating the best datasets for training models given their specific use case, and this is very costly in terms of research and development time. In order to solve this issue, I propose building a tool that leverages LLMs themselves to determine the best datasets to train a model with, collecting them, and storing them, for ease-of-use and to expedite the data science and engineering work required to build these models.

## Demo

https://mediaspace.illinois.edu/media/t/1_1zyoab5w

## Usage

### Save chatbot cookie as JSON file

1. Install the Cookie-Editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
2. Navigate to [Microsoft's Copilot chatbot](https://copilot.microsoft.com/)
3. Open the Cookie-Editor extension
7. Click "Export" on the bottom right, then "Export as JSON" (copies your cookies to clipboard)
8. Paste your cookie into a file such as `copilot_cookies_*.json`

### Run `load.py` and pass in chatbot cookie

`python load.py --cookie-file “./copilot_cookie.json" --prompt “apples”`
