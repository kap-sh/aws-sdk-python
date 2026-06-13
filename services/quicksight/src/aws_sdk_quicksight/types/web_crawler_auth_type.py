"""Generated from Smithy shape ``com.amazonaws.quicksight#WebCrawlerAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WebCrawlerAuthType: TypeAlias = Literal[
    "NO_AUTH",
    "BASIC_AUTH",
    "FORM",
    "SAML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_AUTH",
        "BASIC_AUTH",
        "FORM",
        "SAML",
    )
)


def serialize_json(value: WebCrawlerAuthType) -> str:
    return value


def deserialize_json(data: str) -> WebCrawlerAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebCrawlerAuthType value: {data!r}")
    return cast(WebCrawlerAuthType, data)
