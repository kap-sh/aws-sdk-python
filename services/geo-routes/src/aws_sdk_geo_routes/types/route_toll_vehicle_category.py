"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollVehicleCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTollVehicleCategory: TypeAlias = Literal["Minibus",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Minibus",))


def serialize_json(value: RouteTollVehicleCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteTollVehicleCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTollVehicleCategory value: {data!r}")
    return cast(RouteTollVehicleCategory, data)
