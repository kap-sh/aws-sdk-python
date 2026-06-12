"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSteeringDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSteeringDirection: TypeAlias = Literal[
    "Left",
    "Right",
    "Straight",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Left",
        "Right",
        "Straight",
    )
)


def serialize_json(value: RouteSteeringDirection) -> str:
    return value


def deserialize_json(data: str) -> RouteSteeringDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteSteeringDirection value: {data!r}")
    return cast(RouteSteeringDirection, data)
