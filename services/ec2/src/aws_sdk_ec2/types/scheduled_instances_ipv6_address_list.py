"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIpv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instances_ipv6_address

ScheduledInstancesIpv6AddressList: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instances_ipv6_address.ScheduledInstancesIpv6Address"
]
