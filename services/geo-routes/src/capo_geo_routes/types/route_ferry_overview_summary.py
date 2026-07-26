"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryOverviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds


class RouteFerryOverviewSummary(TypedDict, closed=True):
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryOverviewSummary) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    return out


def deserialize_json(data: dict) -> RouteFerryOverviewSummary:
    out: RouteFerryOverviewSummary = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out
