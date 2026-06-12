"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiMode: TypeAlias = Literal[
    "All",
    "Car",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Car",
    )
)


def serialize_json(value: RouteTaxiMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTaxiMode value: {data!r}")
    return cast(RouteTaxiMode, data)
