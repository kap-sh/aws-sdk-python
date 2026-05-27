"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.event_code
    import aws_sdk_ec2.types.instance_event_id
    import aws_sdk_ec2.types.string


class InstanceStatusEvent(TypedDict):
    instance_event_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_id.InstanceEventId"
    ]
    """<p>The ID of the event.</p>"""
    code: NotRequired["aws_sdk_ec2.types.event_code.EventCode"]
    """<p>The event code.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the event.</p> <p>After a scheduled event is completed, it can still be described for up to a week. If the event has been completed, this description starts with the following text: [Completed].</p>"""
    not_after: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The latest scheduled end time for the event.</p>"""
    not_before: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The earliest scheduled start time for the event.</p>"""
    not_before_deadline: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The deadline for starting the event.</p>"""
