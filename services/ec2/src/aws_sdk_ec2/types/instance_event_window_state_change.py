"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowStateChange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_id
    import aws_sdk_ec2.types.instance_event_window_state


class InstanceEventWindowStateChange(TypedDict):
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""
