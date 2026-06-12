"""Generated from Smithy shape ``com.amazonaws.georoutes#SideOfStreetMatchingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

SideOfStreetMatchingStrategy: TypeAlias = Literal[
    "AnyStreet",
    "DividedStreetOnly",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AnyStreet",
        "DividedStreetOnly",
    )
)


def serialize_json(value: SideOfStreetMatchingStrategy) -> str:
    return value


def deserialize_json(data: str) -> SideOfStreetMatchingStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SideOfStreetMatchingStrategy value: {data!r}"
        )
    return cast(SideOfStreetMatchingStrategy, data)
