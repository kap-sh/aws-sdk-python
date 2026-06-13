"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PreferredDayTimeMaintenanceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.day


class PreferredDayTimeMaintenanceConfiguration(TypedDict):
    day: "aws_sdk_mediaconnect.types.day.Day"
    """<p>The preferred day for maintenance operations.</p>"""
    time: "str"
    """<p>The preferred time for maintenance operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreferredDayTimeMaintenanceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.day

    out["day"] = aws_sdk_mediaconnect.types.day.serialize_json(value["day"])
    out["time"] = value["time"]
    return out


def deserialize_json(data: dict) -> PreferredDayTimeMaintenanceConfiguration:
    out: PreferredDayTimeMaintenanceConfiguration = {}  # type: ignore[typeddict-item]
    if "day" in data:
        import aws_sdk_mediaconnect.types.day

        out["day"] = aws_sdk_mediaconnect.types.day.deserialize_json(data["day"])
    else:
        raise DeserializationError(
            "PreferredDayTimeMaintenanceConfiguration.day required"
        )
    if "time" in data:
        out["time"] = data["time"]
    else:
        raise DeserializationError(
            "PreferredDayTimeMaintenanceConfiguration.time required"
        )
    return out
