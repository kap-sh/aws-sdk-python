"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkEdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_edge

CoreNetworkEdgeList: TypeAlias = list[
    "capo_networkmanager.types.core_network_edge.CoreNetworkEdge"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEdgeList) -> list:
    import capo_networkmanager.types.core_network_edge

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.core_network_edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoreNetworkEdgeList:
    import capo_networkmanager.types.core_network_edge

    out: CoreNetworkEdgeList = []
    for item in data:
        out.append(capo_networkmanager.types.core_network_edge.deserialize_json(item))
    return out
