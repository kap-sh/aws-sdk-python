"""Generated from Smithy shape ``com.amazonaws.ec2#UserIdGroupPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class UserIdGroupPair(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the security group rule that references this user ID group pair.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*</p>"""
    user_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of an Amazon Web Services account.</p> <p>For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>[Default VPC] The name of the security group. For a security group in a nondefault VPC, use the security group ID. </p> <p>For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC for the referenced security group, if applicable.</p>"""
    vpc_peering_connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection, if applicable.</p>"""
    peering_status: NotRequired["capo_ec2.types.string.String"]
    """<p>The status of a VPC peering connection, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserIdGroupPair, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "peering_status" in value:
        pairs.append((f"{prefix}.PeeringStatus", str(value["peering_status"])))


def deserialize_ec2_query(el: Element) -> UserIdGroupPair:
    out: UserIdGroupPair = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_peering_status = el.find("PeeringStatus")
    if child_peering_status is not None:
        out["peering_status"] = str(child_peering_status.text or "")
    return out
