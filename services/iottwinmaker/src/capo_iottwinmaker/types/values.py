"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_value

Values: TypeAlias = list["capo_iottwinmaker.types.property_value.PropertyValue"]


# --- restJson1 ser/de ---
def serialize_json(value: Values) -> list:
    import capo_iottwinmaker.types.property_value

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> Values:
    import capo_iottwinmaker.types.property_value

    out: Values = []
    for item in data:
        out.append(capo_iottwinmaker.types.property_value.deserialize_json(item))
    return out
