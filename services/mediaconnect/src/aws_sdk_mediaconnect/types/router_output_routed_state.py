"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputRoutedState``."""

from typing import Literal, TypeAlias, cast

RouterOutputRoutedState: TypeAlias = Literal[
    "ROUTED",
    "ROUTING",
    "UNROUTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputRoutedState) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputRoutedState:
    return cast(RouterOutputRoutedState, data)
