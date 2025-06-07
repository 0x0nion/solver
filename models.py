from pydantic import BaseModel


class TokenTask(BaseModel):
    website_url: str
    sitekey: str
    action: str
    cdata: str
    pagedata: str
    user_agent: str


class CfClearanceTask(BaseModel):
    website_url: str
    html_base64: str
    user_agent: str
    proxy_type: str
    proxy_address: str
    proxy_port: int
    proxy_login: str
    proxy_password: str