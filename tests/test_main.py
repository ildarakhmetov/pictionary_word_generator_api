import pytest
from unittest.mock import mock_open, patch

from app.main import read_file_of_category, get_words


def test_read_file_of_category_normal():
    # Mock data to be returned by the file read
    mock_data = "apple\nbanana\ncherry"
    category = "fruits"
    
    # Setup the mock
    m = mock_open(read_data=mock_data)

    with patch('builtins.open', m):
        # Call the function
        result = read_file_of_category(category)

    # Verify the result
    assert result == mock_data.split('\n')


def test_read_file_of_category_empty_file():
    category = "empty"
    m = mock_open(read_data="")

    with patch('builtins.open', m):
        result = read_file_of_category(category)

    assert result == []


def test_read_file_of_category_special_characters():
    mock_data = "café\nnaïve\nrésumé"
    category = "special"

    m = mock_open(read_data=mock_data)

    with patch('builtins.open', m):
        result = read_file_of_category(category)

    assert result == mock_data.split('\n')


def test_read_file_of_category_file_not_found():
    category = "nonexistent"

    # Mock the open function to raise FileNotFoundError
    m = mock_open()
    m.side_effect = FileNotFoundError

    with patch('builtins.open', m):
        with pytest.raises(FileNotFoundError):
            read_file_of_category(category)


def test_read_file_of_category_includes_empty_strings():
    mock_data = "apple\nbanana\ncherry\n\n\n"
    category = "fruits"

    m = mock_open(read_data=mock_data)

    with patch('builtins.open', m):
        result = read_file_of_category(category)

    assert result == mock_data.split('\n')[:-3]


def test_get_words_normal():
    category = "animal"
    count = 2
    mock_data = "apple\nbanana"

    m = mock_open(read_data=mock_data)

    with patch('builtins.open', m):
        result = get_words(category, count)

    assert result == {"status": "ok", "words": ["apple", "banana"]}


def test_get_words_invalid_category():
    category = "invalid"
    count = 2

    result = get_words(category, count)

    assert result == {"status": "error", "error": "Category not found"}


def test_get_words_count_none():
    category = "animal"
    count = None
    mock_data = "apple"

    m = mock_open(read_data=mock_data)

    with patch('builtins.open', m):
        result = get_words(category, count)

    assert result == {"status": "ok", "words": ["apple"]}


def test_get_words_count_greater_than_10():
    category = "animal"
    count = 11

    result = get_words(category, count)

    assert result == {"status": "error", "error": "Count must be less or equal than 10"}