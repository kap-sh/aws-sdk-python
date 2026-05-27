"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointSubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_id

CreateVerifiedAccessEndpointSubnetIdList: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_id.SubnetId"
]
