"""Generated from Smithy shape ``com.amazonaws.ec2#ReferencedSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ReferencedSecurityGroup(TypedDict, closed=True):
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    peering_status: NotRequired["capo_ec2.types.string.String"]
    """<p>The status of a VPC peering connection, if applicable.</p>"""
    user_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    vpc_peering_connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection (if applicable).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReferencedSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "peering_status" in value:
        pairs.append((f"{key_prefix}PeeringStatus", str(value["peering_status"])))
    if "user_id" in value:
        pairs.append((f"{key_prefix}UserId", str(value["user_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ReferencedSecurityGroup:
    out: ReferencedSecurityGroup = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_peering_status = el.find("peeringStatus")
    if child_peering_status is not None:
        out["peering_status"] = str(child_peering_status.text or "")
    child_user_id = el.find("userId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_peering_connection_id = el.find("vpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    return out
