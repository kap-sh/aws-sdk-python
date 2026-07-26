"""Generated from Smithy shape ``com.amazonaws.braket#Associations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.association

Associations: TypeAlias = list["capo_braket.types.association.Association"]


# --- restJson1 ser/de ---
def serialize_json(value: Associations) -> list:
    import capo_braket.types.association

    out: list = []
    for item in value:
        out.append(capo_braket.types.association.serialize_json(item))
    return out


def deserialize_json(data: list) -> Associations:
    import capo_braket.types.association

    out: Associations = []
    for item in data:
        out.append(capo_braket.types.association.deserialize_json(item))
    return out
