"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_change_event

CoreNetworkChangeEventList: TypeAlias = list[
    "capo_networkmanager.types.core_network_change_event.CoreNetworkChangeEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeEventList) -> list:
    import capo_networkmanager.types.core_network_change_event

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.core_network_change_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkChangeEventList:
    import capo_networkmanager.types.core_network_change_event

    out: CoreNetworkChangeEventList = []
    for item in data:
        out.append(
            capo_networkmanager.types.core_network_change_event.deserialize_json(item)
        )
    return out
