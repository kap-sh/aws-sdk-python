"""Generated from Smithy shape ``com.amazonaws.iotevents#DeleteAlarmModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_model_name


class DeleteAlarmModelRequest(TypedDict):
    alarm_model_name: "aws_sdk_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAlarmModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAlarmModelRequest:
    out: DeleteAlarmModelRequest = {}  # type: ignore[typeddict-item]
    return out
