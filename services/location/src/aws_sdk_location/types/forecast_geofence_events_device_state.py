"""Generated from Smithy shape ``com.amazonaws.location#ForecastGeofenceEventsDeviceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.position


class ForecastGeofenceEventsDeviceState(TypedDict, closed=True):
    position: "aws_sdk_location.types.position.Position"
    """<p>The device's position.</p>"""
    speed: NotRequired["float"]
    """<p>The device's speed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastGeofenceEventsDeviceState) -> dict:
    out: dict = {}
    import aws_sdk_location.types.position

    out["Position"] = aws_sdk_location.types.position.serialize_json(value["position"])
    if "speed" in value:
        out["Speed"] = value["speed"]
    return out


def deserialize_json(data: dict) -> ForecastGeofenceEventsDeviceState:
    out: ForecastGeofenceEventsDeviceState = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "ForecastGeofenceEventsDeviceState.position required"
        )
    if "Speed" in data:
        out["speed"] = data["Speed"]
    return out
