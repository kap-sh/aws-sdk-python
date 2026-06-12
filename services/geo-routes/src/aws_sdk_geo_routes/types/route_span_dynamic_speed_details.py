"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanDynamicSpeedDetails``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class RouteSpanDynamicSpeedDetails(TypedDict):
    best_case_speed: (
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    )
    """<p>Estimated speed while traversing the span without traffic congestion.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    turn_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Estimated time to turn from this span into the next. </p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    typical_speed: (
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    )
    """<p>Estimated speed while traversing the span under typical traffic congestion.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanDynamicSpeedDetails) -> dict:
    out: dict = {}
    out["BestCaseSpeed"] = value.get("best_case_speed", 0)
    out["TurnDuration"] = value.get("turn_duration", 0)
    out["TypicalSpeed"] = value.get("typical_speed", 0)
    return out


def deserialize_json(data: dict) -> RouteSpanDynamicSpeedDetails:
    out: RouteSpanDynamicSpeedDetails = {}  # type: ignore[typeddict-item]
    if "BestCaseSpeed" in data:
        out["best_case_speed"] = data["BestCaseSpeed"]
    else:
        out["best_case_speed"] = 0
    if "TurnDuration" in data:
        out["turn_duration"] = data["TurnDuration"]
    else:
        out["turn_duration"] = 0
    if "TypicalSpeed" in data:
        out["typical_speed"] = data["TypicalSpeed"]
    else:
        out["typical_speed"] = 0
    return out
