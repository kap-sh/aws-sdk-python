"""Generated from Smithy shape ``com.amazonaws.kendra#WebCrawlerMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

WebCrawlerMode: TypeAlias = Literal[
    "HOST_ONLY",
    "SUBDOMAINS",
    "EVERYTHING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOST_ONLY",
        "SUBDOMAINS",
        "EVERYTHING",
    )
)


def serialize_aws_json_1_1(value: WebCrawlerMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebCrawlerMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebCrawlerMode value: {data!r}")
    return cast(WebCrawlerMode, data)
