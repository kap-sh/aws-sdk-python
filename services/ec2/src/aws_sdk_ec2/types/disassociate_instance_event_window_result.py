"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateInstanceEventWindowResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window


class DisassociateInstanceEventWindowResult(TypedDict):
    instance_event_window: NotRequired[
        "aws_sdk_ec2.types.instance_event_window.InstanceEventWindow"
    ]
    """<p>Information about the event window.</p>"""
