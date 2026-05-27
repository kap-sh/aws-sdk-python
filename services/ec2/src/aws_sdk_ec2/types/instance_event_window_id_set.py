"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_id

InstanceEventWindowIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
]
