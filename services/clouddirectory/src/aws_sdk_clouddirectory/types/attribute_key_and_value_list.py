"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKeyAndValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value

AttributeKeyAndValueList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.attribute_key_and_value.AttributeKeyAndValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKeyAndValueList) -> list:
    import aws_sdk_clouddirectory.types.attribute_key_and_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.attribute_key_and_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttributeKeyAndValueList:
    import aws_sdk_clouddirectory.types.attribute_key_and_value

    out: AttributeKeyAndValueList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.attribute_key_and_value.deserialize_json(item)
        )
    return out
