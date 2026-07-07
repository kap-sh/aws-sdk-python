"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitOverviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds


class RouteTransitOverviewSummary(TypedDict, closed=True):
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitOverviewSummary) -> dict:
    out: dict = {}
    out["Distance"] = value["distance"]
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RouteTransitOverviewSummary:
    out: RouteTransitOverviewSummary = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("RouteTransitOverviewSummary.distance required")
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTransitOverviewSummary.duration required")
    return out
