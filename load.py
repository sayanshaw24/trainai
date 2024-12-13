# Usage: python load.py --cookie-file “./copilot_cookie.json" --prompt “apples”

# Import necessary libraries and modules
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

import argparse
import json
import os
import asyncio
import cv2
import numpy as np

# Leverage Microsoft Copilot to retrieve dataset links
async def chat(args, prompt):
    cookies = json.loads(open(args.cookie_file, encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
    output_text = response["text"]
    await bot.close()
    return output_text


if __name__ == "__main__":

    # Parse arguments for chatbot cookie path and topic prompt
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie-file", help="File containing auth cookie", type=str)
    parser.add_argument(
        "--prompt",
        help="Topic to find datasets for",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    # Load auth cookie
    with open(args.cookie_file, encoding="utf-8") as file:
        cookie_json = json.load(file)
        for cookie in cookie_json:
            if cookie.get("name") == "_U":
                args.U = cookie.get("value")
                break

    if args.cookie-file is None:
        raise Exception("Error: Could not find chatbot cookie")

    # Note: we ping Copilot chat a few times in case we are initially blocked by a Recaptcha check or run into similar issues; this might need to be modified for testing.
    for i in range(3):
        try:
            description = asyncio.run(chat(args, f"give me 10 links to datasets regarding {args.prompt}, but print the whole link url along with the dataset descriptions"))
            print(description + "\n")
            break
        except Exception as e:
            print(e)
            continue
