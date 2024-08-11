# AI-Image-Generator-using-OpenAI-API

This repository contains a Python script that generates images based on user input using the OpenAI API.

## Requirements

- Python 3.x
- OpenAI API key
- `requests` library
- `Pillow` library

# Code Explanation
The script performs the following steps:

- Import Libraries: Imports necessary libraries (openai, requests, Pillow).
- Get API Key: Sets the OpenAI API key.
- Generate Image: Prompts the user for input to generate an image using OpenAI's API.
- Fetch Image URL: Retrieves the URL of the generated image.
- Download and Save Image: Downloads the image from the URL and saves it as image.png.
- Display Image: Opens and displays the saved image.

Install the required packages:
```bash
pip install openai requests pillow

