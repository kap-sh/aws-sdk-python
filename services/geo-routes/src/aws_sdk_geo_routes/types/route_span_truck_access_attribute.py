"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanTruckAccessAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSpanTruckAccessAttribute: TypeAlias = Literal[
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


def serialize_json(value: RouteSpanTruckAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanTruckAccessAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanTruckAccessAttribute value: {data!r}"
        )
    return cast(RouteSpanTruckAccessAttribute, data)
