"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateVpcCidrBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_cidr_block_association
    import capo_ec2.types.vpc_ipv6_cidr_block_association


class DisassociateVpcCidrBlockResult(TypedDict, closed=True):
    ipv6_cidr_block_association: NotRequired[
        "capo_ec2.types.vpc_ipv6_cidr_block_association.VpcIpv6CidrBlockAssociation"
    ]
    """<p>Information about the IPv6 CIDR block association.</p>"""
    cidr_block_association: NotRequired[
        "capo_ec2.types.vpc_cidr_block_association.VpcCidrBlockAssociation"
    ]
    """<p>Information about the IPv4 CIDR block association.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateVpcCidrBlockResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_cidr_block_association" in value:
        import capo_ec2.types.vpc_ipv6_cidr_block_association

        capo_ec2.types.vpc_ipv6_cidr_block_association.serialize_ec2_query(
            value["ipv6_cidr_block_association"],
            pairs,
            f"{prefix}.Ipv6CidrBlockAssociation",
        )
    if "cidr_block_association" in value:
        import capo_ec2.types.vpc_cidr_block_association

        capo_ec2.types.vpc_cidr_block_association.serialize_ec2_query(
            value["cidr_block_association"], pairs, f"{prefix}.CidrBlockAssociation"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> DisassociateVpcCidrBlockResult:
    out: DisassociateVpcCidrBlockResult = {}  # type: ignore[typeddict-item]
    child_ipv6_cidr_block_association = el.find("Ipv6CidrBlockAssociation")
    if child_ipv6_cidr_block_association is not None:
        import capo_ec2.types.vpc_ipv6_cidr_block_association

        out["ipv6_cidr_block_association"] = (
            capo_ec2.types.vpc_ipv6_cidr_block_association.deserialize_ec2_query(
                child_ipv6_cidr_block_association
            )
        )
    child_cidr_block_association = el.find("CidrBlockAssociation")
    if child_cidr_block_association is not None:
        import capo_ec2.types.vpc_cidr_block_association

        out["cidr_block_association"] = (
            capo_ec2.types.vpc_cidr_block_association.deserialize_ec2_query(
                child_cidr_block_association
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
