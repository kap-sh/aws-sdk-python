"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_endpoint_association

VpcEndpointAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_endpoint_association.VpcEndpointAssociation"
]
