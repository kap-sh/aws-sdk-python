"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TimerDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.seconds
    import aws_sdk_iot_events_data.types.timer_name


class TimerDefinition(TypedDict):
    name: "aws_sdk_iot_events_data.types.timer_name.TimerName"
    """<p>The name of the timer.</p>"""
    seconds: "aws_sdk_iot_events_data.types.seconds.Seconds"
    """<p>The new setting of the timer (the number of seconds before the timer elapses).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimerDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["seconds"] = value["seconds"]
    return out


def deserialize_json(data: dict) -> TimerDefinition:
    out: TimerDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TimerDefinition.name required")
    if "seconds" in data:
        out["seconds"] = data["seconds"]
    else:
        raise DeserializationError("TimerDefinition.seconds required")
    return out
