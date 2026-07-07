"""Generated from Smithy shape ``com.amazonaws.pinpoint#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.campaign_event_filter
    import aws_sdk_pinpoint.types.frequency
    import aws_sdk_pinpoint.types.quiet_time


class Schedule(TypedDict, closed=True):
    end_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The scheduled time, in ISO 8601 format, when the campaign ended or will end.</p>"""
    event_filter: NotRequired[
        "aws_sdk_pinpoint.types.campaign_event_filter.CampaignEventFilter"
    ]
    """<p>The type of event that causes the campaign to be sent, if the value of the Frequency property is EVENT.</p>"""
    frequency: NotRequired["aws_sdk_pinpoint.types.frequency.Frequency"]
    """<p>Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.</p>"""
    is_local_time: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the start and end times for the campaign schedule use each recipient's local time. To base the schedule on each recipient's local time, set this value to true.</p>"""
    quiet_time: NotRequired["aws_sdk_pinpoint.types.quiet_time.QuietTime"]
    """<p>The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesn't send messages to endpoints, if all the following conditions are met:</p> <ul><li><p>The EndpointDemographic.Timezone property of the endpoint is set to a valid value.</p></li> <li><p>The current time in the endpoint's time zone is later than or equal to the time specified by the QuietTime.Start property for the campaign.</p></li> <li><p>The current time in the endpoint's time zone is earlier than or equal to the time specified by the QuietTime.End property for the campaign.</p></li></ul> <p>If any of the preceding conditions isn't met, the endpoint will receive messages from the campaign, even if quiet time is enabled.</p>"""
    start_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The scheduled time when the campaign began or will begin. Valid values are: IMMEDIATE, to start the campaign immediately; or, a specific time in ISO 8601 format.</p>"""
    timezone: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The starting UTC offset for the campaign schedule, if the value of the IsLocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10, and UTC-11.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "event_filter" in value:
        import aws_sdk_pinpoint.types.campaign_event_filter

        out["EventFilter"] = (
            aws_sdk_pinpoint.types.campaign_event_filter.serialize_json(
                value["event_filter"]
            )
        )
    if "frequency" in value:
        import aws_sdk_pinpoint.types.frequency

        out["Frequency"] = aws_sdk_pinpoint.types.frequency.serialize_json(
            value["frequency"]
        )
    if "is_local_time" in value:
        out["IsLocalTime"] = value["is_local_time"]
    if "quiet_time" in value:
        import aws_sdk_pinpoint.types.quiet_time

        out["QuietTime"] = aws_sdk_pinpoint.types.quiet_time.serialize_json(
            value["quiet_time"]
        )
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "EventFilter" in data:
        import aws_sdk_pinpoint.types.campaign_event_filter

        out["event_filter"] = (
            aws_sdk_pinpoint.types.campaign_event_filter.deserialize_json(
                data["EventFilter"]
            )
        )
    if "Frequency" in data:
        import aws_sdk_pinpoint.types.frequency

        out["frequency"] = aws_sdk_pinpoint.types.frequency.deserialize_json(
            data["Frequency"]
        )
    if "IsLocalTime" in data:
        out["is_local_time"] = data["IsLocalTime"]
    if "QuietTime" in data:
        import aws_sdk_pinpoint.types.quiet_time

        out["quiet_time"] = aws_sdk_pinpoint.types.quiet_time.deserialize_json(
            data["QuietTime"]
        )
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    return out
