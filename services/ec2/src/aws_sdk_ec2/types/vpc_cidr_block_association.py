"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_cidr_block_state


class VpcCidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association ID for the IPv4 CIDR block.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block.</p>"""
    cidr_block_state: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_state.VpcCidrBlockState"
    ]
    """<p>Information about the state of the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcCidrBlockAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))
    if "cidr_block_state" in value:
        import aws_sdk_ec2.types.vpc_cidr_block_state

        aws_sdk_ec2.types.vpc_cidr_block_state.serialize_ec2_query(
            value["cidr_block_state"], pairs, f"{prefix}.CidrBlockState"
        )


def deserialize_ec2_query(el: Element) -> VpcCidrBlockAssociation:
    out: VpcCidrBlockAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_cidr_block_state = el.find("CidrBlockState")
    if child_cidr_block_state is not None:
        import aws_sdk_ec2.types.vpc_cidr_block_state

        out["cidr_block_state"] = (
            aws_sdk_ec2.types.vpc_cidr_block_state.deserialize_ec2_query(
                child_cidr_block_state
            )
        )
    return out
