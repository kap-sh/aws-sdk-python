"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceIdRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance_id

ScheduledInstanceIdRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instance_id.ScheduledInstanceId"
]
