"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecord``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.event_information
    import aws_sdk_ec2.types.event_type


class HistoryRecord(TypedDict):
    event_information: NotRequired[
        "aws_sdk_ec2.types.event_information.EventInformation"
    ]
    """<p>Information about the event.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.event_type.EventType"]
    """<p>The event type.</p> <ul> <li> <p> <code>error</code> - An error with the Spot Fleet request.</p> </li> <li> <p> <code>fleetRequestChange</code> - A change in the status or configuration of the Spot Fleet request.</p> </li> <li> <p> <code>instanceChange</code> - An instance was launched or terminated.</p> </li> <li> <p> <code>Information</code> - An informational event.</p> </li> </ul>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the event, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
