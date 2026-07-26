"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleOverviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds


class RouteVehicleOverviewSummary(TypedDict, closed=True):
    best_case_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    typical_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the leg under typical traffic congestion.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleOverviewSummary) -> dict:
    out: dict = {}
    out["BestCaseDuration"] = value.get("best_case_duration", 0)
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    out["TypicalDuration"] = value.get("typical_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteVehicleOverviewSummary:
    out: RouteVehicleOverviewSummary = {}  # type: ignore[typeddict-item]
    if "BestCaseDuration" in data:
        out["best_case_duration"] = data["BestCaseDuration"]
    else:
        out["best_case_duration"] = 0
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "TypicalDuration" in data:
        out["typical_duration"] = data["TypicalDuration"]
    else:
        out["typical_duration"] = 0
    return out
