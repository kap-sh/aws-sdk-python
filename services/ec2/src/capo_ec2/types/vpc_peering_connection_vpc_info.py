"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionVpcInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cidr_block_set
    import capo_ec2.types.ipv6_cidr_block_set
    import capo_ec2.types.string
    import capo_ec2.types.vpc_peering_connection_options_description


class VpcPeeringConnectionVpcInfo(TypedDict, closed=True):
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block for the VPC.</p>"""
    ipv6_cidr_block_set: NotRequired[
        "capo_ec2.types.ipv6_cidr_block_set.Ipv6CidrBlockSet"
    ]
    """<p>The IPv6 CIDR block for the VPC.</p>"""
    cidr_block_set: NotRequired["capo_ec2.types.cidr_block_set.CidrBlockSet"]
    """<p>Information about the IPv4 CIDR blocks for the VPC.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC.</p>"""
    peering_options: NotRequired[
        "capo_ec2.types.vpc_peering_connection_options_description.VpcPeeringConnectionOptionsDescription"
    ]
    """<p>Information about the VPC peering connection options for the accepter or requester VPC.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region in which the VPC is located.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcPeeringConnectionVpcInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))
    if "ipv6_cidr_block_set" in value:
        import capo_ec2.types.ipv6_cidr_block_set

        capo_ec2.types.ipv6_cidr_block_set.serialize_ec2_query(
            value["ipv6_cidr_block_set"], pairs, f"{prefix}.Ipv6CidrBlockSet"
        )
    if "cidr_block_set" in value:
        import capo_ec2.types.cidr_block_set

        capo_ec2.types.cidr_block_set.serialize_ec2_query(
            value["cidr_block_set"], pairs, f"{prefix}.CidrBlockSet"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "peering_options" in value:
        import capo_ec2.types.vpc_peering_connection_options_description

        capo_ec2.types.vpc_peering_connection_options_description.serialize_ec2_query(
            value["peering_options"], pairs, f"{prefix}.PeeringOptions"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "region" in value:
        pairs.append((f"{prefix}.Region", str(value["region"])))


def deserialize_ec2_query(el: Element) -> VpcPeeringConnectionVpcInfo:
    out: VpcPeeringConnectionVpcInfo = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    if el.find("Ipv6CidrBlockSet") is not None:
        import capo_ec2.types.ipv6_cidr_block_set

        out["ipv6_cidr_block_set"] = (
            capo_ec2.types.ipv6_cidr_block_set.deserialize_ec2_query(
                el, "Ipv6CidrBlockSet"
            )
        )
    if el.find("CidrBlockSet") is not None:
        import capo_ec2.types.cidr_block_set

        out["cidr_block_set"] = capo_ec2.types.cidr_block_set.deserialize_ec2_query(
            el, "CidrBlockSet"
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_peering_options = el.find("PeeringOptions")
    if child_peering_options is not None:
        import capo_ec2.types.vpc_peering_connection_options_description

        out["peering_options"] = (
            capo_ec2.types.vpc_peering_connection_options_description.deserialize_ec2_query(
                child_peering_options
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    return out
