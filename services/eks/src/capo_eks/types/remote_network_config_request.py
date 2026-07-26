"""Generated from Smithy shape ``com.amazonaws.eks#RemoteNetworkConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.remote_node_network_list
    import capo_eks.types.remote_pod_network_list


class RemoteNetworkConfigRequest(TypedDict, closed=True):
    remote_node_networks: NotRequired[
        "capo_eks.types.remote_node_network_list.RemoteNodeNetworkList"
    ]
    """<p>The list of network CIDRs that can contain hybrid nodes.</p> <p>These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator. </p> <p>Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, <code> 10.2.0.0/16</code>).</p> <p>It must satisfy the following requirements:</p> <ul> <li> <p>Each block must be within an <code>IPv4</code> RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.</p> </li> <li> <p>Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.</p> </li> <li> <p>Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including Transit Gateway, Site-to-Site VPN, or Direct Connect.</p> </li> <li> <p>Each host must allow outbound connection to the EKS cluster control plane on TCP ports <code>443</code> and <code>10250</code>.</p> </li> <li> <p>Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.</p> </li> <li> <p> Each host must allow TCP and UDP network connectivity to and from other hosts that are running <code>CoreDNS</code> on UDP port <code>53</code> for service and pod DNS names.</p> </li> </ul>"""
    remote_pod_networks: NotRequired[
        "capo_eks.types.remote_pod_network_list.RemotePodNetworkList"
    ]
    """<p>The list of network CIDRs that can contain pods that run Kubernetes webhooks on hybrid nodes.</p> <p>These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.</p> <p>Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, <code> 10.2.0.0/16</code>).</p> <p>It must satisfy the following requirements:</p> <ul> <li> <p>Each block must be within an <code>IPv4</code> RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.</p> </li> <li> <p>Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteNetworkConfigRequest) -> dict:
    out: dict = {}
    if "remote_node_networks" in value:
        import capo_eks.types.remote_node_network_list

        out["remoteNodeNetworks"] = (
            capo_eks.types.remote_node_network_list.serialize_json(
                value["remote_node_networks"]
            )
        )
    if "remote_pod_networks" in value:
        import capo_eks.types.remote_pod_network_list

        out["remotePodNetworks"] = (
            capo_eks.types.remote_pod_network_list.serialize_json(
                value["remote_pod_networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoteNetworkConfigRequest:
    out: RemoteNetworkConfigRequest = {}  # type: ignore[typeddict-item]
    if "remoteNodeNetworks" in data:
        import capo_eks.types.remote_node_network_list

        out["remote_node_networks"] = (
            capo_eks.types.remote_node_network_list.deserialize_json(
                data["remoteNodeNetworks"]
            )
        )
    if "remotePodNetworks" in data:
        import capo_eks.types.remote_pod_network_list

        out["remote_pod_networks"] = (
            capo_eks.types.remote_pod_network_list.deserialize_json(
                data["remotePodNetworks"]
            )
        )
    return out
