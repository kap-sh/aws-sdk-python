"""Generated from Smithy shape ``com.amazonaws.iotevents#ResetTimerAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.timer_name


class ResetTimerAction(TypedDict, closed=True):
    timer_name: "capo_iot_events.types.timer_name.TimerName"
    """<p>The name of the timer to reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetTimerAction) -> dict:
    out: dict = {}
    out["timerName"] = value["timer_name"]
    return out


def deserialize_json(data: dict) -> ResetTimerAction:
    out: ResetTimerAction = {}  # type: ignore[typeddict-item]
    if "timerName" in data:
        out["timer_name"] = data["timerName"]
    else:
        raise DeserializationError("ResetTimerAction.timer_name required")
    return out
