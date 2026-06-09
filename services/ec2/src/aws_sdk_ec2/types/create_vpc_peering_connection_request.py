"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcPeeringConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.vpc_id


class CreateVpcPeeringConnectionRequest(TypedDict):
    peer_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</p> <p>Default: The Region in which you make the request.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the peering connection.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the requester VPC. You must specify this parameter in the request.</p>"""
    peer_vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</p>"""
    peer_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the accepter VPC.</p> <p>Default: Your Amazon Web Services account ID</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcPeeringConnectionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "peer_region" in value:
        pairs.append((f"{prefix}.PeerRegion", str(value["peer_region"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "peer_vpc_id" in value:
        pairs.append((f"{prefix}.PeerVpcId", str(value["peer_vpc_id"])))
    if "peer_owner_id" in value:
        pairs.append((f"{prefix}.PeerOwnerId", str(value["peer_owner_id"])))


def deserialize_ec2_query(el: Element) -> CreateVpcPeeringConnectionRequest:
    out: CreateVpcPeeringConnectionRequest = {}  # type: ignore[typeddict-item]
    child_peer_region = el.find("PeerRegion")
    if child_peer_region is not None:
        out["peer_region"] = str(child_peer_region.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_peer_vpc_id = el.find("PeerVpcId")
    if child_peer_vpc_id is not None:
        out["peer_vpc_id"] = str(child_peer_vpc_id.text or "")
    child_peer_owner_id = el.find("PeerOwnerId")
    if child_peer_owner_id is not None:
        out["peer_owner_id"] = str(child_peer_owner_id.text or "")
    return out
