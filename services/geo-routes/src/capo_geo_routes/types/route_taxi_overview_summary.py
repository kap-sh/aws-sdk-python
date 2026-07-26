"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiOverviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds


class RouteTaxiOverviewSummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiOverviewSummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    out["Distance"] = value["distance"]
    return out


def deserialize_json(data: dict) -> RouteTaxiOverviewSummary:
    out: RouteTaxiOverviewSummary = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiOverviewSummary.duration required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("RouteTaxiOverviewSummary.distance required")
    return out
