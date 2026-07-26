"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteState``."""

from typing import Literal, TypeAlias, cast

RouteState: TypeAlias = Literal[
    "ACTIVE",
    "BLACKHOLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteState) -> str:
    return value


def deserialize_json(data: str) -> RouteState:
    return cast(RouteState, data)
