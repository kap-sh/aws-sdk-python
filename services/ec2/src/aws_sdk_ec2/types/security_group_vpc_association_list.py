"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_vpc_association

SecurityGroupVpcAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_vpc_association.SecurityGroupVpcAssociation"
]
