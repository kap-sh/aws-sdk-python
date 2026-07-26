"""Generated from Smithy shape ``com.amazonaws.location#LinearRings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.linear_ring

LinearRings: TypeAlias = list["capo_location.types.linear_ring.LinearRing"]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRings) -> list:
    import capo_location.types.linear_ring

    out: list = []
    for item in value:
        out.append(capo_location.types.linear_ring.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRings:
    import capo_location.types.linear_ring

    out: LinearRings = []
    for item in data:
        out.append(capo_location.types.linear_ring.deserialize_json(item))
    return out
