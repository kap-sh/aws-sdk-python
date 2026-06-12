"""Generated from Smithy shape ``com.amazonaws.iot#SearchableAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.attribute_name

SearchableAttributes: TypeAlias = list["aws_sdk_iot.types.attribute_name.AttributeName"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableAttributes) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchableAttributes:
    return list(data)
