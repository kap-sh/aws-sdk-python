"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSubnetCidrBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.subnet_ipv6_cidr_block_association


class AssociateSubnetCidrBlockResult(TypedDict, closed=True):
    ipv6_cidr_block_association: NotRequired[
        "capo_ec2.types.subnet_ipv6_cidr_block_association.SubnetIpv6CidrBlockAssociation"
    ]
    """<p>Information about the IPv6 association.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateSubnetCidrBlockResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_cidr_block_association" in value:
        import capo_ec2.types.subnet_ipv6_cidr_block_association

        capo_ec2.types.subnet_ipv6_cidr_block_association.serialize_ec2_query(
            value["ipv6_cidr_block_association"],
            pairs,
            f"{key_prefix}Ipv6CidrBlockAssociation",
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))


def deserialize_ec2_query(el: Element) -> AssociateSubnetCidrBlockResult:
    out: AssociateSubnetCidrBlockResult = {}  # type: ignore[typeddict-item]
    child_ipv6_cidr_block_association = el.find("ipv6CidrBlockAssociation")
    if child_ipv6_cidr_block_association is not None:
        import capo_ec2.types.subnet_ipv6_cidr_block_association

        out["ipv6_cidr_block_association"] = (
            capo_ec2.types.subnet_ipv6_cidr_block_association.deserialize_ec2_query(
                child_ipv6_cidr_block_association
            )
        )
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    return out
