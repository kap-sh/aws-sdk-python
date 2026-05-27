"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRangeRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_time_range_request

InstanceEventWindowTimeRangeRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.instance_event_window_time_range_request.InstanceEventWindowTimeRangeRequest"
]
