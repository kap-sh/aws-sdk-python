"""Generated from Smithy shape ``com.amazonaws.datazone#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_input

Attributes: TypeAlias = list["aws_sdk_datazone.types.attribute_input.AttributeInput"]


# --- restJson1 ser/de ---
def serialize_json(value: Attributes) -> list:
    import aws_sdk_datazone.types.attribute_input
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.attribute_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> Attributes:
    import aws_sdk_datazone.types.attribute_input
    out: Attributes = []
    for item in data:
        out.append(aws_sdk_datazone.types.attribute_input.deserialize_json(item))
    return out