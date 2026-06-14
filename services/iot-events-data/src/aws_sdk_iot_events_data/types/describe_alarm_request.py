"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DescribeAlarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_model_name
    import aws_sdk_iot_events_data.types.key_value


class DescribeAlarmRequest(TypedDict):
    alarm_model_name: "aws_sdk_iot_events_data.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    r"""<p>The value of the key used as a filter to select only the alarms associated with the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\">key</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAlarmRequest:
    out: DescribeAlarmRequest = {}  # type: ignore[typeddict-item]
    return out
