"""Generated from Smithy shape ``com.amazonaws.connect#Subtypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.subtype

Subtypes: TypeAlias = list["capo_connect.types.subtype.Subtype"]


# --- restJson1 ser/de ---
def serialize_json(value: Subtypes) -> list:
    return list(value)


def deserialize_json(data: list) -> Subtypes:
    return list(data)
