"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAttachmentFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluenceAttachmentFieldName: TypeAlias = Literal[
    "AUTHOR",
    "CONTENT_TYPE",
    "CREATED_DATE",
    "DISPLAY_URL",
    "FILE_SIZE",
    "ITEM_TYPE",
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
        "CONTENT_TYPE",
        "CREATED_DATE",
        "DISPLAY_URL",
        "FILE_SIZE",
        "ITEM_TYPE",
        "PARENT_ID",
        "SPACE_KEY",
        "SPACE_NAME",
        "URL",
        "VERSION",
    )
)


def serialize_aws_json_1_1(value: ConfluenceAttachmentFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceAttachmentFieldName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfluenceAttachmentFieldName value: {data!r}"
        )
    return cast(ConfluenceAttachmentFieldName, data)
