"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecordEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.event_information
    import aws_sdk_ec2.types.fleet_event_type


class HistoryRecordEntry(TypedDict):
    event_information: NotRequired[
        "aws_sdk_ec2.types.event_information.EventInformation"
    ]
    """<p>Information about the event.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.fleet_event_type.FleetEventType"]
    """<p>The event type.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the event, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
