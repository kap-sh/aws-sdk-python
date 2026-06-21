"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanRoadAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanRoadAttribute: TypeAlias = Literal[
    "Bridge",
    "BuiltUpArea",
    "ControlledAccessHighway",
    "DirtRoad",
    "DividedRoad",
    "Motorway",
    "PrivateRoad",
    "Ramp",
    "RightHandTraffic",
    "Roundabout",
    "Tunnel",
    "UnderConstruction",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanRoadAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanRoadAttribute:
    return cast(RouteSpanRoadAttribute, data)
