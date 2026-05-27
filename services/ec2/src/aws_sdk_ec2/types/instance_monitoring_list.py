"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMonitoringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_monitoring

InstanceMonitoringList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_monitoring.InstanceMonitoring"
]
