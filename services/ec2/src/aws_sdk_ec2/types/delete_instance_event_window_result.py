"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceEventWindowResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_state_change


class DeleteInstanceEventWindowResult(TypedDict):
    instance_event_window_state: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_state_change.InstanceEventWindowStateChange"
    ]
    """<p>The state of the event window.</p>"""
