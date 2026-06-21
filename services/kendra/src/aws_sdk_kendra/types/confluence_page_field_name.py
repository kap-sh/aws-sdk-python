"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluencePageFieldName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ConfluencePageFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluencePageFieldName:
    return cast(ConfluencePageFieldName, data)
