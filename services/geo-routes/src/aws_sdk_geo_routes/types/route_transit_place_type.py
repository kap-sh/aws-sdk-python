"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitPlaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitPlaceType: TypeAlias = Literal["Station",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Station",))


def serialize_json(value: RouteTransitPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitPlaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTransitPlaceType value: {data!r}")
    return cast(RouteTransitPlaceType, data)
