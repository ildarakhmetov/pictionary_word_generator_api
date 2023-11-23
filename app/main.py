from typing import Union
from fastapi import FastAPI
import random

app = FastAPI()


def read_file_of_category(category: str):
    """
    Reads a file of a category and returns a list of words
    """
    with open(f"words/{category}.txt", "r") as f:
        res = f.read().split("\n")

        # Remove empty strings
        res = list(filter(None, res))
        res = list(filter(lambda x: x != "", res))

        if res == [""]:
            return []
        return res


@app.get("/words/{category}/random")
def get_words(category: str, count: Union[int, None] = None):
    if category not in ["animal", "hard", "object", "people", "place", "verb"]:
        return {"status": "error", "error": "Category not found"}
    if count is None:
        count = 1
    if count > 10:
        return {"status": "error", "error": "Count must be less or equal than 10"}

    # Read the file
    words = read_file_of_category(category)

    # Get random count words
    random_words = random.sample(words, count)

    # Return the words
    return {"status": "ok", "words": random_words}
