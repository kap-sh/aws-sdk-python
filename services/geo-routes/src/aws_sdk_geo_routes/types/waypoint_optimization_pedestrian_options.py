"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationPedestrianOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class WaypointOptimizationPedestrianOptions(TypedDict, closed=True):
    speed: NotRequired[
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationPedestrianOptions) -> dict:
    out: dict = {}
    if "speed" in value:
        out["Speed"] = value["speed"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationPedestrianOptions:
    out: WaypointOptimizationPedestrianOptions = {}  # type: ignore[typeddict-item]
    if "Speed" in data:
        out["speed"] = data["Speed"]
    return out
