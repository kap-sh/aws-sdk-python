"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetIpv4CidrBlockAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet_ipv4_cidr_block_association

SecondarySubnetIpv4CidrBlockAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_subnet_ipv4_cidr_block_association.SecondarySubnetIpv4CidrBlockAssociation"
]
