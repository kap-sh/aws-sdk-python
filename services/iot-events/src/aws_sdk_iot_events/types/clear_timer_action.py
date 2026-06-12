"""Generated from Smithy shape ``com.amazonaws.iotevents#ClearTimerAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.timer_name


class ClearTimerAction(TypedDict):
    timer_name: "aws_sdk_iot_events.types.timer_name.TimerName"
    """<p>The name of the timer to clear.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClearTimerAction) -> dict:
    out: dict = {}
    out["timerName"] = value["timer_name"]
    return out


def deserialize_json(data: dict) -> ClearTimerAction:
    out: ClearTimerAction = {}  # type: ignore[typeddict-item]
    if "timerName" in data:
        out["timer_name"] = data["timerName"]
    else:
        raise DeserializationError("ClearTimerAction.timer_name required")
    return out
