"""Generated from Smithy shape ``com.amazonaws.eks#RemoteNetworkConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.remote_node_network_list
    import aws_sdk_eks.types.remote_pod_network_list


class RemoteNetworkConfigResponse(TypedDict, closed=True):
    remote_node_networks: NotRequired[
        "aws_sdk_eks.types.remote_node_network_list.RemoteNodeNetworkList"
    ]
    """<p>The list of network CIDRs that can contain hybrid nodes.</p>"""
    remote_pod_networks: NotRequired[
        "aws_sdk_eks.types.remote_pod_network_list.RemotePodNetworkList"
    ]
    """<p>The list of network CIDRs that can contain pods that run Kubernetes webhooks on hybrid nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteNetworkConfigResponse) -> dict:
    out: dict = {}
    if "remote_node_networks" in value:
        import aws_sdk_eks.types.remote_node_network_list

        out["remoteNodeNetworks"] = (
            aws_sdk_eks.types.remote_node_network_list.serialize_json(
                value["remote_node_networks"]
            )
        )
    if "remote_pod_networks" in value:
        import aws_sdk_eks.types.remote_pod_network_list

        out["remotePodNetworks"] = (
            aws_sdk_eks.types.remote_pod_network_list.serialize_json(
                value["remote_pod_networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoteNetworkConfigResponse:
    out: RemoteNetworkConfigResponse = {}  # type: ignore[typeddict-item]
    if "remoteNodeNetworks" in data:
        import aws_sdk_eks.types.remote_node_network_list

        out["remote_node_networks"] = (
            aws_sdk_eks.types.remote_node_network_list.deserialize_json(
                data["remoteNodeNetworks"]
            )
        )
    if "remotePodNetworks" in data:
        import aws_sdk_eks.types.remote_pod_network_list

        out["remote_pod_networks"] = (
            aws_sdk_eks.types.remote_pod_network_list.deserialize_json(
                data["remotePodNetworks"]
            )
        )
    return out
