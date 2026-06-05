"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpv6CidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association

SubnetIpv6CidrBlockAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_ipv6_cidr_block_association.SubnetIpv6CidrBlockAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetIpv6CidrBlockAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association

        aws_sdk_ec2.types.subnet_ipv6_cidr_block_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SubnetIpv6CidrBlockAssociationSet:
    import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association

    out: SubnetIpv6CidrBlockAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.subnet_ipv6_cidr_block_association.deserialize_ec2_query(
                child
            )
        )
    return out
