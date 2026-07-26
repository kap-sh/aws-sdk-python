"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ClusterNode(TypedDict, closed=True):
    node_role: NotRequired["capo_redshift.types.string.String"]
    """<p>Whether the node is a leader node or a compute node.</p>"""
    private_ip_address: NotRequired["capo_redshift.types.string.String"]
    """<p>The private IP address of a node within a cluster.</p>"""
    public_ip_address: NotRequired["capo_redshift.types.string.String"]
    """<p>The public IP address of a node within a cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterNode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "node_role" in value:
        pairs.append((f"{prefix}.NodeRole", str(value["node_role"])))
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIPAddress", str(value["private_ip_address"])))
    if "public_ip_address" in value:
        pairs.append((f"{prefix}.PublicIPAddress", str(value["public_ip_address"])))


def deserialize_query(el: Element) -> ClusterNode:
    out: ClusterNode = {}  # type: ignore[typeddict-item]
    child_node_role = el.find("NodeRole")
    if child_node_role is not None:
        out["node_role"] = str(child_node_role.text or "")
    child_private_ip_address = el.find("PrivateIPAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_public_ip_address = el.find("PublicIPAddress")
    if child_public_ip_address is not None:
        out["public_ip_address"] = str(child_public_ip_address.text or "")
    return out
