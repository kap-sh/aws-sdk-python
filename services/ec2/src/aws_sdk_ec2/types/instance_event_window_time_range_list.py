"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_time_range

InstanceEventWindowTimeRangeList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_event_window_time_range.InstanceEventWindowTimeRange"
]
