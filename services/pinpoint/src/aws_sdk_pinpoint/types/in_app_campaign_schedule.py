"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppCampaignSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.campaign_event_filter
    import aws_sdk_pinpoint.types.quiet_time


class InAppCampaignSchedule(TypedDict, closed=True):
    end_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The scheduled time after which the in-app message should not be shown. Timestamp is in ISO 8601 format.</p>"""
    event_filter: NotRequired[
        "aws_sdk_pinpoint.types.campaign_event_filter.CampaignEventFilter"
    ]
    """<p>The event filter the SDK has to use to show the in-app message in the application.</p>"""
    quiet_time: NotRequired["aws_sdk_pinpoint.types.quiet_time.QuietTime"]
    """<p>Time during which the in-app message should not be shown to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppCampaignSchedule) -> dict:
    out: dict = {}
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    if "event_filter" in value:
        import aws_sdk_pinpoint.types.campaign_event_filter

        out["EventFilter"] = (
            aws_sdk_pinpoint.types.campaign_event_filter.serialize_json(
                value["event_filter"]
            )
        )
    if "quiet_time" in value:
        import aws_sdk_pinpoint.types.quiet_time

        out["QuietTime"] = aws_sdk_pinpoint.types.quiet_time.serialize_json(
            value["quiet_time"]
        )
    return out


def deserialize_json(data: dict) -> InAppCampaignSchedule:
    out: InAppCampaignSchedule = {}  # type: ignore[typeddict-item]
    if "EndDate" in data:
        out["end_date"] = data["EndDate"]
    if "EventFilter" in data:
        import aws_sdk_pinpoint.types.campaign_event_filter

        out["event_filter"] = (
            aws_sdk_pinpoint.types.campaign_event_filter.deserialize_json(
                data["EventFilter"]
            )
        )
    if "QuietTime" in data:
        import aws_sdk_pinpoint.types.quiet_time

        out["quiet_time"] = aws_sdk_pinpoint.types.quiet_time.deserialize_json(
            data["QuietTime"]
        )
    return out
