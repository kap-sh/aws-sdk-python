"""Generated from Smithy shape ``com.amazonaws.eks#RemotePodNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.remote_pod_network

RemotePodNetworkList: TypeAlias = list[
    "aws_sdk_eks.types.remote_pod_network.RemotePodNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemotePodNetworkList) -> list:
    import aws_sdk_eks.types.remote_pod_network

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.remote_pod_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemotePodNetworkList:
    import aws_sdk_eks.types.remote_pod_network

    out: RemotePodNetworkList = []
    for item in data:
        out.append(aws_sdk_eks.types.remote_pod_network.deserialize_json(item))
    return out
