"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerMonitoredTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key

CapacityManagerMonitoredTagKeyList: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_monitored_tag_key.CapacityManagerMonitoredTagKey"
]
