"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTimeBreakdown``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds


class WaypointOptimizationTimeBreakdown(TypedDict):
    rest_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Resting phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    service_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Service time spent at the destination. At an appointment, the service time should be the appointment duration.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    travel_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Traveling phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    wait_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Waiting phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTimeBreakdown) -> dict:
    out: dict = {}
    out["RestDuration"] = value.get("rest_duration", 0)
    out["ServiceDuration"] = value.get("service_duration", 0)
    out["TravelDuration"] = value.get("travel_duration", 0)
    out["WaitDuration"] = value.get("wait_duration", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTimeBreakdown:
    out: WaypointOptimizationTimeBreakdown = {}  # type: ignore[typeddict-item]
    if "RestDuration" in data:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    if "ServiceDuration" in data:
        out["service_duration"] = data["ServiceDuration"]
    else:
        out["service_duration"] = 0
    if "TravelDuration" in data:
        out["travel_duration"] = data["TravelDuration"]
    else:
        out["travel_duration"] = 0
    if "WaitDuration" in data:
        out["wait_duration"] = data["WaitDuration"]
    else:
        out["wait_duration"] = 0
    return out
