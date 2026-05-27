"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportsImageIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id

DescribeImageUsageReportsImageIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.image_id.ImageId"
]
