"""Generated from Smithy shape ``com.amazonaws.connect#AttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.attribute

AttributesList: TypeAlias = list["capo_connect.types.attribute.Attribute"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributesList) -> list:
    import capo_connect.types.attribute

    out: list = []
    for item in value:
        out.append(capo_connect.types.attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributesList:
    import capo_connect.types.attribute

    out: AttributesList = []
    for item in data:
        out.append(capo_connect.types.attribute.deserialize_json(item))
    return out
