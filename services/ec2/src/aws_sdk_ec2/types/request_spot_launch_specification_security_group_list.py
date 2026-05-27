"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotLaunchSpecificationSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

RequestSpotLaunchSpecificationSecurityGroupList: TypeAlias = list[
    "aws_sdk_ec2.types.string.String"
]
