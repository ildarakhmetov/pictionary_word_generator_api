# Pictionary Word Generator REST API

This is a REST API for generating random words for the game Pictionary. It is created for a student project at Northeasten University. However, it is free to use for anyone. Just keep in mind that it's deployed on a free Render server, so it may not be the fastest.

## Usage

The API is hosted at https://pictionary-word-generator.onrender.com/.

Docs: https://pictionary-word-generator.onrender.com/docs.

## Endpoints

### GET /words/:category/random

Returns a random word from the specified category.

If the `count` query parameter is specified, it will return that many words. The maximum value for `count` is 10.

#### Categories

- `animal`
- `object`
- `verb`
- `place`
- `people`
- `hard`

#### Examples

Request:

```
GET https://pictionary-word-generator.onrender.com/words/animal/random
```

Response:

```json
{
    "status": "ok",
    "words": [
        "Shark"
    ]
}
```

Request:

```
GET https://pictionary-word-generator.onrender.com/words/animal/random?count=3
```

Response:

```json
{
    "status": "ok",
    "words": [
        "Shark",
        "Pig",
        "Lion"
    ]
}
```

Request:

```
GET https://pictionary-word-generator.onrender.com/words/invalid/random
```

Response:

```json
{
    "status": "error",
    "message": "Category not found"
}
```

