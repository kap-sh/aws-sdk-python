"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_id
    import capo_ec2.types.security_group_vpc_association_state
    import capo_ec2.types.string
    import capo_ec2.types.vpc_id


class SecurityGroupVpcAssociation(TypedDict, closed=True):
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The association's security group ID.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The association's VPC ID.</p>"""
    vpc_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the VPC.</p>"""
    state: NotRequired[
        "capo_ec2.types.security_group_vpc_association_state.SecurityGroupVpcAssociationState"
    ]
    """<p>The association's state.</p>"""
    state_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The association's state reason.</p>"""
    group_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the security group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupVpcAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpc_owner_id" in value:
        pairs.append((f"{key_prefix}VpcOwnerId", str(value["vpc_owner_id"])))
    if "state" in value:
        import capo_ec2.types.security_group_vpc_association_state

        capo_ec2.types.security_group_vpc_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "group_owner_id" in value:
        pairs.append((f"{key_prefix}GroupOwnerId", str(value["group_owner_id"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupVpcAssociation:
    out: SecurityGroupVpcAssociation = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_owner_id = el.find("VpcOwnerId")
    if child_vpc_owner_id is not None:
        out["vpc_owner_id"] = str(child_vpc_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.security_group_vpc_association_state

        out["state"] = (
            capo_ec2.types.security_group_vpc_association_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_group_owner_id = el.find("GroupOwnerId")
    if child_group_owner_id is not None:
        out["group_owner_id"] = str(child_group_owner_id.text or "")
    return out
