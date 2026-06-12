"""Generated from Smithy shape ``com.amazonaws.iotevents#ListAlarmModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_model_summaries
    import aws_sdk_iot_events.types.next_token


class ListAlarmModelsResponse(TypedDict):
    alarm_model_summaries: NotRequired[
        "aws_sdk_iot_events.types.alarm_model_summaries.AlarmModelSummaries"
    ]
    """<p>A list that summarizes each alarm model.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlarmModelsResponse) -> dict:
    out: dict = {}
    if "alarm_model_summaries" in value:
        import aws_sdk_iot_events.types.alarm_model_summaries

        out["alarmModelSummaries"] = (
            aws_sdk_iot_events.types.alarm_model_summaries.serialize_json(
                value["alarm_model_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlarmModelsResponse:
    out: ListAlarmModelsResponse = {}  # type: ignore[typeddict-item]
    if "alarmModelSummaries" in data:
        import aws_sdk_iot_events.types.alarm_model_summaries

        out["alarm_model_summaries"] = (
            aws_sdk_iot_events.types.alarm_model_summaries.deserialize_json(
                data["alarmModelSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
