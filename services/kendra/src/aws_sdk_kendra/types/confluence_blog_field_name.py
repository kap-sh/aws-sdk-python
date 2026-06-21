"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceBlogFieldName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ConfluenceBlogFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceBlogFieldName:
    return cast(ConfluenceBlogFieldName, data)
