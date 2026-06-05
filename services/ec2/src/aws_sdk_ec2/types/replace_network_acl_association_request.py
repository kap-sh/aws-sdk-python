"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceNetworkAclAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_acl_association_id
    import aws_sdk_ec2.types.network_acl_id


class ReplaceNetworkAclAssociationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    association_id: NotRequired[
        "aws_sdk_ec2.types.network_acl_association_id.NetworkAclAssociationId"
    ]
    """<p>The ID of the current association between the original network ACL and the subnet.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.network_acl_id.NetworkAclId"]
    """<p>The ID of the new network ACL to associate with the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceNetworkAclAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "network_acl_id" in value:
        pairs.append((f"{prefix}.NetworkAclId", str(value["network_acl_id"])))


def deserialize_ec2_query(el: Element) -> ReplaceNetworkAclAssociationRequest:
    out: ReplaceNetworkAclAssociationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_network_acl_id = el.find("NetworkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    return out
