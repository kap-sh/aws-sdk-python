"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluencePageFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluencePageFieldName: TypeAlias = Literal[
    "AUTHOR",
    "CONTENT_STATUS",
    "CREATED_DATE",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "MODIFIED_DATE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHOR",
        "CONTENT_STATUS",
        "CREATED_DATE",
        "DISPLAY_URL",
        "ITEM_TYPE",
        "LABELS",
        "MODIFIED_DATE",
        "PARENT_ID",
        "SPACE_KEY",
        "SPACE_NAME",
        "URL",
        "VERSION",
    )
)


def serialize_aws_json_1_1(value: ConfluencePageFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluencePageFieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluencePageFieldName value: {data!r}")
    return cast(ConfluencePageFieldName, data)
