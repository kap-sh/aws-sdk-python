"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_value

PropertyValues: TypeAlias = list["capo_iottwinmaker.types.property_value.PropertyValue"]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValues) -> list:
    import capo_iottwinmaker.types.property_value

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertyValues:
    import capo_iottwinmaker.types.property_value

    out: PropertyValues = []
    for item in data:
        out.append(capo_iottwinmaker.types.property_value.deserialize_json(item))
    return out
