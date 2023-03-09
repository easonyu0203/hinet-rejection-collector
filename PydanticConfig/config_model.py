from pydantic import BaseModel


class ImapConfig(BaseModel):
    user: str
    password: str
    imap_url: str


class Config(BaseModel):
    imap: ImapConfig



