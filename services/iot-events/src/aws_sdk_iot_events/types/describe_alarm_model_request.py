"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeAlarmModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_model_name
    import aws_sdk_iot_events.types.alarm_model_version


class DescribeAlarmModelRequest(TypedDict):
    alarm_model_name: "aws_sdk_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    alarm_model_version: NotRequired[
        "aws_sdk_iot_events.types.alarm_model_version.AlarmModelVersion"
    ]
    """<p>The version of the alarm model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAlarmModelRequest:
    out: DescribeAlarmModelRequest = {}  # type: ignore[typeddict-item]
    return out
