"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class RoutePedestrianOptions(TypedDict):
    speed: NotRequired[
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed in Kilometers per hour.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianOptions) -> dict:
    out: dict = {}
    if "speed" in value:
        out["Speed"] = value["speed"]
    return out


def deserialize_json(data: dict) -> RoutePedestrianOptions:
    out: RoutePedestrianOptions = {}  # type: ignore[typeddict-item]
    if "Speed" in data:
        out["speed"] = data["Speed"]
    return out
