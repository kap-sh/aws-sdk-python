"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutingObjective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoutingObjective: TypeAlias = Literal[
    "FastestRoute",
    "ShortestRoute",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FastestRoute",
        "ShortestRoute",
    )
)


def serialize_json(value: RoutingObjective) -> str:
    return value


def deserialize_json(data: str) -> RoutingObjective:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingObjective value: {data!r}")
    return cast(RoutingObjective, data)
