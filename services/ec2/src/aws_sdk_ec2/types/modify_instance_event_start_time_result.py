"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventStartTimeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_event


class ModifyInstanceEventStartTimeResult(TypedDict):
    event: NotRequired["aws_sdk_ec2.types.instance_status_event.InstanceStatusEvent"]
    """<p>Information about the event.</p>"""
