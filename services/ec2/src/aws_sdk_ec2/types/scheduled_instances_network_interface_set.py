"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesNetworkInterfaceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instances_network_interface

ScheduledInstancesNetworkInterfaceSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instances_network_interface.ScheduledInstancesNetworkInterface"
]
