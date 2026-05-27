"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_cidr_association

Ipv6CidrAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipv6_cidr_association.Ipv6CidrAssociation"
]
