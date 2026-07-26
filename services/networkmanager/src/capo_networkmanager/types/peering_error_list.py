"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.peering_error

PeeringErrorList: TypeAlias = list[
    "capo_networkmanager.types.peering_error.PeeringError"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringErrorList) -> list:
    import capo_networkmanager.types.peering_error

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.peering_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeeringErrorList:
    import capo_networkmanager.types.peering_error

    out: PeeringErrorList = []
    for item in data:
        out.append(capo_networkmanager.types.peering_error.deserialize_json(item))
    return out
