"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ListAlarmsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_summaries
    import aws_sdk_iot_events_data.types.next_token


class ListAlarmsResponse(TypedDict, closed=True):
    alarm_summaries: NotRequired[
        "aws_sdk_iot_events_data.types.alarm_summaries.AlarmSummaries"
    ]
    """<p>A list that summarizes each alarm.</p>"""
    next_token: NotRequired["aws_sdk_iot_events_data.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlarmsResponse) -> dict:
    out: dict = {}
    if "alarm_summaries" in value:
        import aws_sdk_iot_events_data.types.alarm_summaries

        out["alarmSummaries"] = (
            aws_sdk_iot_events_data.types.alarm_summaries.serialize_json(
                value["alarm_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlarmsResponse:
    out: ListAlarmsResponse = {}  # type: ignore[typeddict-item]
    if "alarmSummaries" in data:
        import aws_sdk_iot_events_data.types.alarm_summaries

        out["alarm_summaries"] = (
            aws_sdk_iot_events_data.types.alarm_summaries.deserialize_json(
                data["alarmSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
