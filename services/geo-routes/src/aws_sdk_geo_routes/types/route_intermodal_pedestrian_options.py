"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalPedestrianOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class RouteIntermodalPedestrianOptions(TypedDict):
    max_distance: NotRequired["aws_sdk_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>Maximum walking distance allowed.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    speed: NotRequired[
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalPedestrianOptions) -> dict:
    out: dict = {}
    if "max_distance" in value:
        out["MaxDistance"] = value["max_distance"]
    if "speed" in value:
        out["Speed"] = value["speed"]
    return out


def deserialize_json(data: dict) -> RouteIntermodalPedestrianOptions:
    out: RouteIntermodalPedestrianOptions = {}  # type: ignore[typeddict-item]
    if "MaxDistance" in data:
        out["max_distance"] = data["MaxDistance"]
    if "Speed" in data:
        out["speed"] = data["Speed"]
    return out
