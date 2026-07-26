"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeAlarmModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_model_name
    import capo_iot_events.types.alarm_model_version


class DescribeAlarmModelRequest(TypedDict, closed=True):
    alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    alarm_model_version: NotRequired[
        "capo_iot_events.types.alarm_model_version.AlarmModelVersion"
    ]
    """<p>The version of the alarm model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAlarmModelRequest:
    out: DescribeAlarmModelRequest = {}  # type: ignore[typeddict-item]
    return out
