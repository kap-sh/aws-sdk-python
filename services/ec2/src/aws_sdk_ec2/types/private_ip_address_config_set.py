"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressConfigSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instances_private_ip_address_config

PrivateIpAddressConfigSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instances_private_ip_address_config.ScheduledInstancesPrivateIpAddressConfig"
]
