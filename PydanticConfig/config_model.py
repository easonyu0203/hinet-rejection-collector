from pydantic import BaseModel


class ImapConfig(BaseModel):
    """configuration relative to IMAP"""
    user: str
    password: str
    imap_url: str


class Config(BaseModel):
    """represent the configuration of the application"""
    imap: ImapConfig



