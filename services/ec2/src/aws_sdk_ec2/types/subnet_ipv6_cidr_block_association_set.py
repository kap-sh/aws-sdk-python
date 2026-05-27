"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpv6CidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association

SubnetIpv6CidrBlockAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_ipv6_cidr_block_association.SubnetIpv6CidrBlockAssociation"
]
