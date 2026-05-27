"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class VolumeStatusEvent(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the event.</p>"""
    event_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of this event.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of this event.</p>"""
    not_after: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The latest end time of the event.</p>"""
    not_before: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest start time of the event.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance associated with the event.</p>"""
