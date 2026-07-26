"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetIpv4CidrBlockAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association

SecondarySubnetIpv4CidrBlockAssociationList: TypeAlias = list[
    "capo_ec2.types.secondary_subnet_ipv4_cidr_block_association.SecondarySubnetIpv4CidrBlockAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondarySubnetIpv4CidrBlockAssociationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association

        capo_ec2.types.secondary_subnet_ipv4_cidr_block_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SecondarySubnetIpv4CidrBlockAssociationList:
    import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association

    out: SecondarySubnetIpv4CidrBlockAssociationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.secondary_subnet_ipv4_cidr_block_association.deserialize_ec2_query(
                child
            )
        )
    return out
