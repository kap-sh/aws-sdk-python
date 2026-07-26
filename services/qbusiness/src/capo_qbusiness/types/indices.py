"""Generated from Smithy shape ``com.amazonaws.qbusiness#Indices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.index

Indices: TypeAlias = list["capo_qbusiness.types.index.Index"]


# --- restJson1 ser/de ---
def serialize_json(value: Indices) -> list:
    import capo_qbusiness.types.index

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.index.serialize_json(item))
    return out


def deserialize_json(data: list) -> Indices:
    import capo_qbusiness.types.index

    out: Indices = []
    for item in data:
        out.append(capo_qbusiness.types.index.deserialize_json(item))
    return out
