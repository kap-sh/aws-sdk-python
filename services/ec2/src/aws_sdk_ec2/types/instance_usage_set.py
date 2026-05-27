"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceUsageSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_usage

InstanceUsageSet: TypeAlias = list["aws_sdk_ec2.types.instance_usage.InstanceUsage"]
