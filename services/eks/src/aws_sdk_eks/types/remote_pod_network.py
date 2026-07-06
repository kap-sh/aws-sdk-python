"""Generated from Smithy shape ``com.amazonaws.eks#RemotePodNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string_list


class RemotePodNetwork(TypedDict, closed=True):
    cidrs: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.</p> <p>These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.</p> <p>Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, <code> 10.2.0.0/16</code>).</p> <p>It must satisfy the following requirements:</p> <ul> <li> <p>Each block must be within an <code>IPv4</code> RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.</p> </li> <li> <p>Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemotePodNetwork) -> dict:
    out: dict = {}
    if "cidrs" in value:
        import aws_sdk_eks.types.string_list

        out["cidrs"] = aws_sdk_eks.types.string_list.serialize_json(value["cidrs"])
    return out


def deserialize_json(data: dict) -> RemotePodNetwork:
    out: RemotePodNetwork = {}  # type: ignore[typeddict-item]
    if "cidrs" in data:
        import aws_sdk_eks.types.string_list

        out["cidrs"] = aws_sdk_eks.types.string_list.deserialize_json(data["cidrs"])
    return out
