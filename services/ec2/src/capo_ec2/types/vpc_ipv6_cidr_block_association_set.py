"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIpv6CidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_ipv6_cidr_block_association

VpcIpv6CidrBlockAssociationSet: TypeAlias = list[
    "capo_ec2.types.vpc_ipv6_cidr_block_association.VpcIpv6CidrBlockAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcIpv6CidrBlockAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_ipv6_cidr_block_association

        capo_ec2.types.vpc_ipv6_cidr_block_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VpcIpv6CidrBlockAssociationSet:
    import capo_ec2.types.vpc_ipv6_cidr_block_association

    out: VpcIpv6CidrBlockAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.vpc_ipv6_cidr_block_association.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VpcIpv6CidrBlockAssociationSet:
    import capo_ec2.types.vpc_ipv6_cidr_block_association

    out: VpcIpv6CidrBlockAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpc_ipv6_cidr_block_association.deserialize_ec2_query(child)
        )
    return out
