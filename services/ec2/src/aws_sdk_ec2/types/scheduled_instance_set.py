"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance

ScheduledInstanceSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instance.ScheduledInstance"
]
