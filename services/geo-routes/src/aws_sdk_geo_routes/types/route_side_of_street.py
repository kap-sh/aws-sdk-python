"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSideOfStreet``."""

from typing import Literal, TypeAlias, cast

RouteSideOfStreet: TypeAlias = Literal[
    "Left",
    "Right",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSideOfStreet) -> str:
    return value


def deserialize_json(data: str) -> RouteSideOfStreet:
    return cast(RouteSideOfStreet, data)
