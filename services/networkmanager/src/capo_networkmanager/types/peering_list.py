"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.peering

PeeringList: TypeAlias = list["capo_networkmanager.types.peering.Peering"]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringList) -> list:
    import capo_networkmanager.types.peering

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.peering.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeeringList:
    import capo_networkmanager.types.peering

    out: PeeringList = []
    for item in data:
        out.append(capo_networkmanager.types.peering.deserialize_json(item))
    return out
