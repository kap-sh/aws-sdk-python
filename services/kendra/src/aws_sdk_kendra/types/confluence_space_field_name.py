"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceSpaceFieldName``."""

from typing import Literal, TypeAlias, cast

ConfluenceSpaceFieldName: TypeAlias = Literal[
    "DISPLAY_URL",
    "ITEM_TYPE",
    "SPACE_KEY",
    "URL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceSpaceFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceSpaceFieldName:
    return cast(ConfluenceSpaceFieldName, data)
