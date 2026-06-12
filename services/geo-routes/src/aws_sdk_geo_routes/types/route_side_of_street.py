"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSideOfStreet``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteSideOfStreet: TypeAlias = Literal[
    "Left",
    "Right",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Left",
        "Right",
    )
)


def serialize_json(value: RouteSideOfStreet) -> str:
    return value


def deserialize_json(data: str) -> RouteSideOfStreet:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteSideOfStreet value: {data!r}")
    return cast(RouteSideOfStreet, data)
