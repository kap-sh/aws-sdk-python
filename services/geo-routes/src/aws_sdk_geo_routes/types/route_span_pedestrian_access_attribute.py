"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanPedestrianAccessAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanPedestrianAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "Indoors",
    "NoThroughTraffic",
    "Park",
    "Stairs",
    "TollRoad",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allowed",
        "Indoors",
        "NoThroughTraffic",
        "Park",
        "Stairs",
        "TollRoad",
    )
)


def serialize_json(value: RouteSpanPedestrianAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanPedestrianAccessAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanPedestrianAccessAttribute value: {data!r}"
        )
    return cast(RouteSpanPedestrianAccessAttribute, data)
