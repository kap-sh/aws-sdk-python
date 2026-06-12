"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_value

PropertyValues: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.property_value.PropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValues) -> list:
    import aws_sdk_iottwinmaker.types.property_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertyValues:
    import aws_sdk_iottwinmaker.types.property_value

    out: PropertyValues = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.property_value.deserialize_json(item))
    return out
