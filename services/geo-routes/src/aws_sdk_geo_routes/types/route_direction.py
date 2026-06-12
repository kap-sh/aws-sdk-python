"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteDirection: TypeAlias = Literal[
    "East",
    "North",
    "South",
    "West",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "East",
        "North",
        "South",
        "West",
    )
)


def serialize_json(value: RouteDirection) -> str:
    return value


def deserialize_json(data: str) -> RouteDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteDirection value: {data!r}")
    return cast(RouteDirection, data)
