"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Timer``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.timer_name
    import aws_sdk_iot_events_data.types.timestamp


class Timer(TypedDict):
    name: "aws_sdk_iot_events_data.types.timer_name.TimerName"
    """<p>The name of the timer.</p>"""
    timestamp: "aws_sdk_iot_events_data.types.timestamp.Timestamp"
    """<p>The expiration time for the timer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Timer) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_iot_events_data.types.timestamp

    out["timestamp"] = aws_sdk_iot_events_data.types.timestamp.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> Timer:
    out: Timer = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Timer.name required")
    if "timestamp" in data:
        import aws_sdk_iot_events_data.types.timestamp

        out["timestamp"] = aws_sdk_iot_events_data.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("Timer.timestamp required")
    return out
