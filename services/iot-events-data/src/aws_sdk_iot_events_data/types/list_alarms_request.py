"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ListAlarmsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_model_name
    import aws_sdk_iot_events_data.types.max_results
    import aws_sdk_iot_events_data.types.next_token


class ListAlarmsRequest(TypedDict, closed=True):
    alarm_model_name: "aws_sdk_iot_events_data.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    next_token: NotRequired["aws_sdk_iot_events_data.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot_events_data.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlarmsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAlarmsRequest:
    out: ListAlarmsRequest = {}  # type: ignore[typeddict-item]
    return out
