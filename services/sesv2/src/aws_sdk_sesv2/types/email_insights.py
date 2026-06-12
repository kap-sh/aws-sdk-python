"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailInsights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.insights_email_address
    import aws_sdk_sesv2.types.insights_events
    import aws_sdk_sesv2.types.isp


class EmailInsights(TypedDict):
    destination: NotRequired[
        "aws_sdk_sesv2.types.insights_email_address.InsightsEmailAddress"
    ]
    """<p>The recipient of the email.</p>"""
    isp: NotRequired["aws_sdk_sesv2.types.isp.Isp"]
    """<p>The recipient's ISP (e.g., <code>Gmail</code>, <code>Yahoo</code>, etc.).</p>"""
    events: NotRequired["aws_sdk_sesv2.types.insights_events.InsightsEvents"]
    """<p>A list of events associated with the sent email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailInsights) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "isp" in value:
        out["Isp"] = value["isp"]
    if "events" in value:
        import aws_sdk_sesv2.types.insights_events

        out["Events"] = aws_sdk_sesv2.types.insights_events.serialize_json(
            value["events"]
        )
    return out


def deserialize_json(data: dict) -> EmailInsights:
    out: EmailInsights = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "Isp" in data:
        out["isp"] = data["Isp"]
    if "Events" in data:
        import aws_sdk_sesv2.types.insights_events

        out["events"] = aws_sdk_sesv2.types.insights_events.deserialize_json(
            data["Events"]
        )
    return out
