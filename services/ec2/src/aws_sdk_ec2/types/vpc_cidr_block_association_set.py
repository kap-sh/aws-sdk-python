"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_cidr_block_association

VpcCidrBlockAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_cidr_block_association.VpcCidrBlockAssociation"
]
