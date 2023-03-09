import pathlib
import pytest
import json
from config_loader.load_json_config import load_json_config


@pytest.fixture
def temp_imap_config_file(tmp_path: pathlib.Path) -> pathlib.Path:
    """
    Create a temporary config file for testing that only contains the 'imap' section.

    This fixture creates a temporary config file with a single 'imap' section, and returns the path to the file.

    Args:
        tmp_path (pathlib.Path): A temporary directory provided by pytest.

    Returns:
        pathlib.Path: The path to the temporary config file.

    """
    config_file = tmp_path / 'test_config.json'
    data = {'imap': {'user': 'test_user', 'password': 'test_password', 'imap_url': 'test_url'}}
    with open(config_file, 'w') as f:
        f.write(json.dumps(data))
    return config_file


def test_load_json_config_contains_imap_section(temp_imap_config_file):
    """
    Test that the 'load_json_config' function correctly loads a config file containing the 'imap' section.

    The test creates a temporary config file with a single 'imap' section, and then verifies that the 'load_json_config'
    function correctly loads the data into a Pydantic object. The test also checks that the resulting Pydantic object
    contains the 'imap' section of the config data, and no additional fields.

    Args:
        temp_imap_config_file (pathlib.Path): A temporary file containing a JSON-encoded 'imap' section.

    """
    # Arrange
    expected_user = 'test_user'
    expected_password = 'test_password'
    expected_url = 'test_url'

    # Act
    config = load_json_config(temp_imap_config_file)

    # Assert
    assert config.imap.user == expected_user
    assert config.imap.password == expected_password
    assert config.imap.imap_url == expected_url
    assert len(config.dict()) == 1
    assert 'imap' in config.dict()
