"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#EnableAlarmActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_model_name
    import aws_sdk_iot_events_data.types.key_value
    import aws_sdk_iot_events_data.types.note
    import aws_sdk_iot_events_data.types.request_id


class EnableAlarmActionRequest(TypedDict, closed=True):
    request_id: "aws_sdk_iot_events_data.types.request_id.RequestId"
    """<p>The request ID. Each ID must be unique within each batch.</p>"""
    alarm_model_name: "aws_sdk_iot_events_data.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    r"""<p>The value of the key used as a filter to select only the alarms associated with the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\">key</a>.</p>"""
    note: NotRequired["aws_sdk_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you enable the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableAlarmActionRequest) -> dict:
    out: dict = {}
    out["requestId"] = value["request_id"]
    out["alarmModelName"] = value["alarm_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> EnableAlarmActionRequest:
    out: EnableAlarmActionRequest = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("EnableAlarmActionRequest.request_id required")
    if "alarmModelName" in data:
        out["alarm_model_name"] = data["alarmModelName"]
    else:
        raise DeserializationError("EnableAlarmActionRequest.alarm_model_name required")
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    if "note" in data:
        out["note"] = data["note"]
    return out
