"""Generated from Smithy shape ``com.amazonaws.sesv2#InsightsEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.event_details
    import aws_sdk_sesv2.types.event_type
    import aws_sdk_sesv2.types.timestamp


class InsightsEvent(TypedDict, closed=True):
    timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of the event.</p>"""
    type: NotRequired["aws_sdk_sesv2.types.event_type.EventType"]
    """<p>The type of event:</p> <ul> <li> <p> <code>SEND</code> - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.) </p> </li> <li> <p> <code>DELIVERY</code> - SES successfully delivered the email to the recipient's mail server. Excludes deliveries to the mailbox simulator, and those from emails addressed to more than one recipient. </p> </li> <li> <p> <code>BOUNCE</code> - Feedback received for delivery failures. Additional details about the bounce are provided in the <code>Details</code> object. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient. </p> </li> <li> <p> <code>COMPLAINT</code> - Complaint received for the email. Additional details about the complaint are provided in the <code>Details</code> object. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient. </p> </li> <li> <p> <code>OPEN</code> - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> </ul>"""
    details: NotRequired["aws_sdk_sesv2.types.event_details.EventDetails"]
    """<p>Details about bounce or complaint events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsEvent) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["Timestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "type" in value:
        import aws_sdk_sesv2.types.event_type

        out["Type"] = aws_sdk_sesv2.types.event_type.serialize_json(value["type"])
    if "details" in value:
        import aws_sdk_sesv2.types.event_details

        out["Details"] = aws_sdk_sesv2.types.event_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> InsightsEvent:
    out: InsightsEvent = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "Type" in data:
        import aws_sdk_sesv2.types.event_type

        out["type"] = aws_sdk_sesv2.types.event_type.deserialize_json(data["Type"])
    if "Details" in data:
        import aws_sdk_sesv2.types.event_details

        out["details"] = aws_sdk_sesv2.types.event_details.deserialize_json(
            data["Details"]
        )
    return out
