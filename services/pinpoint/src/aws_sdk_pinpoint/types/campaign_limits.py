"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignLimits``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer


class CampaignLimits(TypedDict):
    daily: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100.</p>"""
    maximum_duration: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.</p>"""
    messages_per_second: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000.</p>"""
    total: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100.</p>"""
    session: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum total number of messages that the campaign can send per user session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignLimits) -> dict:
    out: dict = {}
    if "daily" in value:
        out["Daily"] = value["daily"]
    if "maximum_duration" in value:
        out["MaximumDuration"] = value["maximum_duration"]
    if "messages_per_second" in value:
        out["MessagesPerSecond"] = value["messages_per_second"]
    if "total" in value:
        out["Total"] = value["total"]
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_json(data: dict) -> CampaignLimits:
    out: CampaignLimits = {}  # type: ignore[typeddict-item]
    if "Daily" in data:
        out["daily"] = data["Daily"]
    if "MaximumDuration" in data:
        out["maximum_duration"] = data["MaximumDuration"]
    if "MessagesPerSecond" in data:
        out["messages_per_second"] = data["MessagesPerSecond"]
    if "Total" in data:
        out["total"] = data["Total"]
    if "Session" in data:
        out["session"] = data["Session"]
    return out
