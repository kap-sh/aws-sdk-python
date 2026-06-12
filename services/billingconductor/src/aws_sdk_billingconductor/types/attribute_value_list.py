"""Generated from Smithy shape ``com.amazonaws.billingconductor#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.attribute_value

AttributeValueList: TypeAlias = list[
    "aws_sdk_billingconductor.types.attribute_value.AttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeValueList:
    return list(data)
