"""Generated from Smithy shape ``com.amazonaws.eks#RemoteNodeNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.remote_node_network

RemoteNodeNetworkList: TypeAlias = list[
    "aws_sdk_eks.types.remote_node_network.RemoteNodeNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteNodeNetworkList) -> list:
    import aws_sdk_eks.types.remote_node_network

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.remote_node_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemoteNodeNetworkList:
    import aws_sdk_eks.types.remote_node_network

    out: RemoteNodeNetworkList = []
    for item in data:
        out.append(aws_sdk_eks.types.remote_node_network.deserialize_json(item))
    return out
