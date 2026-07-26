"""Generated from Smithy shape ``com.amazonaws.georoutes#SideOfStreetMatchingStrategy``."""

from typing import Literal, TypeAlias, cast

SideOfStreetMatchingStrategy: TypeAlias = Literal[
    "AnyStreet",
    "DividedStreetOnly",
]


# --- restJson1 ser/de ---
def serialize_json(value: SideOfStreetMatchingStrategy) -> str:
    return value


def deserialize_json(data: str) -> SideOfStreetMatchingStrategy:
    return cast(SideOfStreetMatchingStrategy, data)
