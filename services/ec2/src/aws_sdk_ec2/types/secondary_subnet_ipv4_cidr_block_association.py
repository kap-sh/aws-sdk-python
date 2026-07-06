"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetIpv4CidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet_cidr_association_id
    import aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state
    import aws_sdk_ec2.types.string


class SecondarySubnetIpv4CidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_cidr_association_id.SecondarySubnetCidrAssociationId"
    ]
    """<p>The association ID for the IPv4 CIDR block.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state.SecondarySubnetCidrBlockAssociationState"
    ]
    """<p>The state of the CIDR block association.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state of the CIDR block association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondarySubnetIpv4CidrBlockAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))
    if "state" in value:
        import aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state

        aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_reason" in value:
        pairs.append((f"{prefix}.StateReason", str(value["state_reason"])))


def deserialize_ec2_query(el: Element) -> SecondarySubnetIpv4CidrBlockAssociation:
    out: SecondarySubnetIpv4CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state

        out["state"] = (
            aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    return out
