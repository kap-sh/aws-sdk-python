"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network

GlobalNetworkList: TypeAlias = list[
    "capo_networkmanager.types.global_network.GlobalNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalNetworkList) -> list:
    import capo_networkmanager.types.global_network

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.global_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> GlobalNetworkList:
    import capo_networkmanager.types.global_network

    out: GlobalNetworkList = []
    for item in data:
        out.append(capo_networkmanager.types.global_network.deserialize_json(item))
    return out
