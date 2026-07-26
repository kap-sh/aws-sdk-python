"""Generated from Smithy shape ``com.amazonaws.efs#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.destination

Destinations: TypeAlias = list["capo_efs.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: Destinations) -> list:
    import capo_efs.types.destination

    out: list = []
    for item in value:
        out.append(capo_efs.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> Destinations:
    import capo_efs.types.destination

    out: Destinations = []
    for item in data:
        out.append(capo_efs.types.destination.deserialize_json(item))
    return out
