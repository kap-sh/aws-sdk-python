"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name

AttributeNameList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeNameList:
    return list(data)
