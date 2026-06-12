"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key

AttributeKeyList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.attribute_key.AttributeKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKeyList) -> list:
    import aws_sdk_clouddirectory.types.attribute_key

    out: list = []
    for item in value:
        out.append(aws_sdk_clouddirectory.types.attribute_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeKeyList:
    import aws_sdk_clouddirectory.types.attribute_key

    out: AttributeKeyList = []
    for item in data:
        out.append(aws_sdk_clouddirectory.types.attribute_key.deserialize_json(item))
    return out
