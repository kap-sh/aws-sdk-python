"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceAvailabilitySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance_availability

ScheduledInstanceAvailabilitySet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instance_availability.ScheduledInstanceAvailability"
]
