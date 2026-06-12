"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeNameAndValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name_and_value

AttributeNameAndValueList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.attribute_name_and_value.AttributeNameAndValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameAndValueList) -> list:
    import aws_sdk_clouddirectory.types.attribute_name_and_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.attribute_name_and_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttributeNameAndValueList:
    import aws_sdk_clouddirectory.types.attribute_name_and_value

    out: AttributeNameAndValueList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.attribute_name_and_value.deserialize_json(item)
        )
    return out
