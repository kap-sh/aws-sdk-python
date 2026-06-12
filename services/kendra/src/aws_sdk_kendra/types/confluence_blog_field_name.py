"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceBlogFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluenceBlogFieldName: TypeAlias = Literal[
    "AUTHOR",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "PUBLISH_DATE",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHOR",
        "DISPLAY_URL",
        "ITEM_TYPE",
        "LABELS",
        "PUBLISH_DATE",
        "SPACE_KEY",
        "SPACE_NAME",
        "URL",
        "VERSION",
    )
)


def serialize_aws_json_1_1(value: ConfluenceBlogFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceBlogFieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluenceBlogFieldName value: {data!r}")
    return cast(ConfluenceBlogFieldName, data)
