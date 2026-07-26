"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetworkIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id

GlobalNetworkIdList: TypeAlias = list[
    "capo_networkmanager.types.global_network_id.GlobalNetworkId"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalNetworkIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GlobalNetworkIdList:
    return list(data)
