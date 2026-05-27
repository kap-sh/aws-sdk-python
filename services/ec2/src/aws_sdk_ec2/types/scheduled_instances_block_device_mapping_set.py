"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesBlockDeviceMappingSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instances_block_device_mapping

ScheduledInstancesBlockDeviceMappingSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instances_block_device_mapping.ScheduledInstancesBlockDeviceMapping"
]
