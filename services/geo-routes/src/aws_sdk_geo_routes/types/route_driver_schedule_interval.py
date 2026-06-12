"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDriverScheduleInterval``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds


class RouteDriverScheduleInterval(TypedDict):
    drive_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Maximum allowed driving time before stopping to rest.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    rest_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Resting time before the driver can continue driving.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDriverScheduleInterval) -> dict:
    out: dict = {}
    out["DriveDuration"] = value.get("drive_duration", 0)
    out["RestDuration"] = value.get("rest_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteDriverScheduleInterval:
    out: RouteDriverScheduleInterval = {}  # type: ignore[typeddict-item]
    if "DriveDuration" in data:
        out["drive_duration"] = data["DriveDuration"]
    else:
        out["drive_duration"] = 0
    if "RestDuration" in data:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    return out
