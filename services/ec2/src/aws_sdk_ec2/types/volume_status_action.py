"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class VolumeStatusAction(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The code identifying the operation, for example, <code>enable-volume-io</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the operation.</p>"""
    event_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the event associated with this operation.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The event type associated with this operation.</p>"""
