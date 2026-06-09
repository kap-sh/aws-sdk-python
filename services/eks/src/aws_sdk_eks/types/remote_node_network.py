"""Generated from Smithy shape ``com.amazonaws.eks#RemoteNodeNetwork``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string_list


class RemoteNodeNetwork(TypedDict):
    cidrs: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A network CIDR that can contain hybrid nodes.</p> <p>These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator. </p> <p>Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, <code> 10.2.0.0/16</code>).</p> <p>It must satisfy the following requirements:</p> <ul> <li> <p>Each block must be within an <code>IPv4</code> RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.</p> </li> <li> <p>Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.</p> </li> <li> <p>Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including Transit Gateway, Site-to-Site VPN, or Direct Connect.</p> </li> <li> <p>Each host must allow outbound connection to the EKS cluster control plane on TCP ports <code>443</code> and <code>10250</code>.</p> </li> <li> <p>Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.</p> </li> <li> <p> Each host must allow TCP and UDP network connectivity to and from other hosts that are running <code>CoreDNS</code> on UDP port <code>53</code> for service and pod DNS names.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteNodeNetwork) -> dict:
    out: dict = {}
    if "cidrs" in value:
        import aws_sdk_eks.types.string_list

        out["cidrs"] = aws_sdk_eks.types.string_list.serialize_json(value["cidrs"])
    return out


def deserialize_json(data: dict) -> RemoteNodeNetwork:
    out: RemoteNodeNetwork = {}  # type: ignore[typeddict-item]
    if "cidrs" in data:
        import aws_sdk_eks.types.string_list

        out["cidrs"] = aws_sdk_eks.types.string_list.deserialize_json(data["cidrs"])
    return out
