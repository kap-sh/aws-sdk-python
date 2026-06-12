"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanScooterAccessAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanScooterAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "NoThroughTraffic",
    "TollRoad",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allowed",
        "NoThroughTraffic",
        "TollRoad",
    )
)


def serialize_json(value: RouteSpanScooterAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanScooterAccessAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanScooterAccessAttribute value: {data!r}"
        )
    return cast(RouteSpanScooterAccessAttribute, data)
