"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelOnlySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RouteVehicleTravelOnlySummary(TypedDict, closed=True):
    best_case_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    typical_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the leg under typical traffic congestion.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleTravelOnlySummary) -> dict:
    out: dict = {}
    out["BestCaseDuration"] = value.get("best_case_duration", 0)
    out["Duration"] = value.get("duration", 0)
    out["TypicalDuration"] = value.get("typical_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteVehicleTravelOnlySummary:
    out: RouteVehicleTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if "BestCaseDuration" in data:
        out["best_case_duration"] = data["BestCaseDuration"]
    else:
        out["best_case_duration"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "TypicalDuration" in data:
        out["typical_duration"] = data["TypicalDuration"]
    else:
        out["typical_duration"] = 0
    return out
