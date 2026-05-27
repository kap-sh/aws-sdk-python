"""Generated from Smithy shape ``com.amazonaws.ec2#ConversionIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task_id

ConversionIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.conversion_task_id.ConversionTaskId"
]
