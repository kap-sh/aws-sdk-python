"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanRoadAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteSpanRoadAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanRoadAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteSpanRoadAttribute value: {data!r}")
    return cast(RouteSpanRoadAttribute, data)
