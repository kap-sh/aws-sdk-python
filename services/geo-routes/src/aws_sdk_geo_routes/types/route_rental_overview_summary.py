"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalOverviewSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds


class RouteRentalOverviewSummary(TypedDict):
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalOverviewSummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    out["Distance"] = value["distance"]
    return out


def deserialize_json(data: dict) -> RouteRentalOverviewSummary:
    out: RouteRentalOverviewSummary = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteRentalOverviewSummary.duration required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("RouteRentalOverviewSummary.distance required")
    return out
