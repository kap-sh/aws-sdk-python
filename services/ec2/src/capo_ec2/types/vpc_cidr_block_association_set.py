"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_cidr_block_association

VpcCidrBlockAssociationSet: TypeAlias = list[
    "capo_ec2.types.vpc_cidr_block_association.VpcCidrBlockAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcCidrBlockAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_cidr_block_association

        capo_ec2.types.vpc_cidr_block_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpcCidrBlockAssociationSet:
    import capo_ec2.types.vpc_cidr_block_association

    out: VpcCidrBlockAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpc_cidr_block_association.deserialize_ec2_query(child)
        )
    return out
