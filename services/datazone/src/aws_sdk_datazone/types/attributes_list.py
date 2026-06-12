"""Generated from Smithy shape ``com.amazonaws.datazone#AttributesList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_identifier

AttributesList: TypeAlias = list["aws_sdk_datazone.types.attribute_identifier.AttributeIdentifier"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributesList:
    return list(data)