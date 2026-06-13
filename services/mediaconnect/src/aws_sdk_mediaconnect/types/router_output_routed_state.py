"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputRoutedState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterOutputRoutedState: TypeAlias = Literal[
    "ROUTED",
    "ROUTING",
    "UNROUTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROUTED",
        "ROUTING",
        "UNROUTED",
    )
)


def serialize_json(value: RouterOutputRoutedState) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputRoutedState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterOutputRoutedState value: {data!r}")
    return cast(RouterOutputRoutedState, data)
