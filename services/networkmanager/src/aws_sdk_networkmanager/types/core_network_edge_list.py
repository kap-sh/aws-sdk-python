"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkEdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_edge

CoreNetworkEdgeList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_edge.CoreNetworkEdge"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEdgeList) -> list:
    import aws_sdk_networkmanager.types.core_network_edge

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.core_network_edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoreNetworkEdgeList:
    import aws_sdk_networkmanager.types.core_network_edge

    out: CoreNetworkEdgeList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_edge.deserialize_json(item)
        )
    return out
