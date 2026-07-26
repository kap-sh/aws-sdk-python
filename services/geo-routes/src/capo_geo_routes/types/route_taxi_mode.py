"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiMode``."""

from typing import Literal, TypeAlias, cast

RouteTaxiMode: TypeAlias = Literal[
    "All",
    "Car",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiMode:
    return cast(RouteTaxiMode, data)
