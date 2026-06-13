"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterInputTier: TypeAlias = Literal[
    "INPUT_100",
    "INPUT_50",
    "INPUT_20",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPUT_100",
        "INPUT_50",
        "INPUT_20",
    )
)


def serialize_json(value: RouterInputTier) -> str:
    return value


def deserialize_json(data: str) -> RouterInputTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterInputTier value: {data!r}")
    return cast(RouterInputTier, data)
