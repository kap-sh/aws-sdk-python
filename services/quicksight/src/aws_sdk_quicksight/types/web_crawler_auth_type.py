"""Generated from Smithy shape ``com.amazonaws.quicksight#WebCrawlerAuthType``."""

from typing import Literal, TypeAlias, cast

WebCrawlerAuthType: TypeAlias = Literal[
    "NO_AUTH",
    "BASIC_AUTH",
    "FORM",
    "SAML",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerAuthType) -> str:
    return value


def deserialize_json(data: str) -> WebCrawlerAuthType:
    return cast(WebCrawlerAuthType, data)
