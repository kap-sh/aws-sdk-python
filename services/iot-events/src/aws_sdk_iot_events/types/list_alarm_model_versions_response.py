"""Generated from Smithy shape ``com.amazonaws.iotevents#ListAlarmModelVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_model_version_summaries
    import aws_sdk_iot_events.types.next_token


class ListAlarmModelVersionsResponse(TypedDict, closed=True):
    alarm_model_version_summaries: NotRequired[
        "aws_sdk_iot_events.types.alarm_model_version_summaries.AlarmModelVersionSummaries"
    ]
    """<p>A list that summarizes each alarm model version.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlarmModelVersionsResponse) -> dict:
    out: dict = {}
    if "alarm_model_version_summaries" in value:
        import aws_sdk_iot_events.types.alarm_model_version_summaries

        out["alarmModelVersionSummaries"] = (
            aws_sdk_iot_events.types.alarm_model_version_summaries.serialize_json(
                value["alarm_model_version_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlarmModelVersionsResponse:
    out: ListAlarmModelVersionsResponse = {}  # type: ignore[typeddict-item]
    if "alarmModelVersionSummaries" in data:
        import aws_sdk_iot_events.types.alarm_model_version_summaries

        out["alarm_model_version_summaries"] = (
            aws_sdk_iot_events.types.alarm_model_version_summaries.deserialize_json(
                data["alarmModelVersionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
