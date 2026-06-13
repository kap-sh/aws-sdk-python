"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterOutputTier: TypeAlias = Literal[
    "OUTPUT_100",
    "OUTPUT_50",
    "OUTPUT_20",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUTPUT_100",
        "OUTPUT_50",
        "OUTPUT_20",
    )
)


def serialize_json(value: RouterOutputTier) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterOutputTier value: {data!r}")
    return cast(RouterOutputTier, data)
