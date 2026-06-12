"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValuesSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.primary_attribute_value

PrimaryAttributeValuesSet: TypeAlias = list[
    "aws_sdk_connect.types.primary_attribute_value.PrimaryAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValuesSet) -> list:
    import aws_sdk_connect.types.primary_attribute_value

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.primary_attribute_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrimaryAttributeValuesSet:
    import aws_sdk_connect.types.primary_attribute_value

    out: PrimaryAttributeValuesSet = []
    for item in data:
        out.append(aws_sdk_connect.types.primary_attribute_value.deserialize_json(item))
    return out
