"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanCarAccessAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanCarAccessAttribute: TypeAlias = Literal[
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


def serialize_json(value: RouteSpanCarAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanCarAccessAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanCarAccessAttribute value: {data!r}"
        )
    return cast(RouteSpanCarAccessAttribute, data)
