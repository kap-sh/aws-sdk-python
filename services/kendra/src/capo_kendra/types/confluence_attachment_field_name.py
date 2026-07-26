"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAttachmentFieldName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ConfluenceAttachmentFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceAttachmentFieldName:
    return cast(ConfluenceAttachmentFieldName, data)
