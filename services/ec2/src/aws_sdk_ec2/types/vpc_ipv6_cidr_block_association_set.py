"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIpv6CidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_ipv6_cidr_block_association

VpcIpv6CidrBlockAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_ipv6_cidr_block_association.VpcIpv6CidrBlockAssociation"
]
