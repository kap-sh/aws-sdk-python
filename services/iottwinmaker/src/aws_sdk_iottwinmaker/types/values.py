"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_value

Values: TypeAlias = list["aws_sdk_iottwinmaker.types.property_value.PropertyValue"]


# --- restJson1 ser/de ---
def serialize_json(value: Values) -> list:
    import aws_sdk_iottwinmaker.types.property_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> Values:
    import aws_sdk_iottwinmaker.types.property_value

    out: Values = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.property_value.deserialize_json(item))
    return out
