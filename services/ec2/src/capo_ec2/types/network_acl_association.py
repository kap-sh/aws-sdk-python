"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class NetworkAclAssociation(TypedDict, closed=True):
    network_acl_association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the association between a network ACL and a subnet.</p>"""
    network_acl_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network ACL.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAclAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_acl_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkAclAssociationId",
                str(value["network_acl_association_id"]),
            )
        )
    if "network_acl_id" in value:
        pairs.append((f"{key_prefix}NetworkAclId", str(value["network_acl_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))


def deserialize_ec2_query(el: Element) -> NetworkAclAssociation:
    out: NetworkAclAssociation = {}  # type: ignore[typeddict-item]
    child_network_acl_association_id = el.find("networkAclAssociationId")
    if child_network_acl_association_id is not None:
        out["network_acl_association_id"] = str(
            child_network_acl_association_id.text or ""
        )
    child_network_acl_id = el.find("networkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    return out
