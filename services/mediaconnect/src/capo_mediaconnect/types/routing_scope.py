"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RoutingScope``."""

from typing import Literal, TypeAlias, cast

RoutingScope: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingScope) -> str:
    return value


def deserialize_json(data: str) -> RoutingScope:
    return cast(RoutingScope, data)
