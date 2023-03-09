from config_loader.config_model import ImapConfig, Config


def test_ImapConfig_should_parse_imap_data() -> None:
    """
    Test the ImapConfig Pydantic model.

    This test checks that the ImapConfig model is correctly parsing a dictionary into a Pydantic object.

    Returns:
        None
    """
    # Arrange
    imap_data = {'user': 'test_user', 'password': 'test_password', 'imap_url': 'test_url'}

    # Act
    imap = ImapConfig.parse_obj(imap_data)

    # Assert
    assert imap.user == 'test_user'
    assert imap.password == 'test_password'
    assert imap.imap_url == 'test_url'


def test_Config_should_parse_config_data_with_imap() -> None:
    """
    Test the Config Pydantic model.

    This test checks that the Config model is correctly parsing a dictionary into a Pydantic object.

    Returns:
        None
    """
    # Arrange
    imap_data = {'user': 'test_user', 'password': 'test_password', 'imap_url': 'test_url'}
    config_data = {'imap': imap_data}

    # Act
    config = Config.parse_obj(config_data)

    # Assert
    assert config.imap.user == 'test_user'
    assert config.imap.password == 'test_password'
    assert config.imap.imap_url == 'test_url'
