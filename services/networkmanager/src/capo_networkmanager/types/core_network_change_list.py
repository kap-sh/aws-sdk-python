"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_change

CoreNetworkChangeList: TypeAlias = list[
    "capo_networkmanager.types.core_network_change.CoreNetworkChange"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeList) -> list:
    import capo_networkmanager.types.core_network_change

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.core_network_change.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoreNetworkChangeList:
    import capo_networkmanager.types.core_network_change

    out: CoreNetworkChangeList = []
    for item in data:
        out.append(capo_networkmanager.types.core_network_change.deserialize_json(item))
    return out
