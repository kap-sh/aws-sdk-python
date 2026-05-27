"""Generated from Smithy shape ``com.amazonaws.ec2#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn

ArnList: TypeAlias = list["aws_sdk_ec2.types.resource_arn.ResourceArn"]
