"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task

DescribeConversionTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.conversion_task.ConversionTask"
]
