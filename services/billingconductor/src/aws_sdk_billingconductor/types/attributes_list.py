"""Generated from Smithy shape ``com.amazonaws.billingconductor#AttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.attribute

AttributesList: TypeAlias = list["aws_sdk_billingconductor.types.attribute.Attribute"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributesList) -> list:
    import aws_sdk_billingconductor.types.attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_billingconductor.types.attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributesList:
    import aws_sdk_billingconductor.types.attribute

    out: AttributesList = []
    for item in data:
        out.append(aws_sdk_billingconductor.types.attribute.deserialize_json(item))
    return out
