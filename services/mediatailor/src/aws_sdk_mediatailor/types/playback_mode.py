"""Generated from Smithy shape ``com.amazonaws.mediatailor#PlaybackMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

PlaybackMode: TypeAlias = Literal[
    "LOOP",
    "LINEAR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOOP",
        "LINEAR",
    )
)


def serialize_json(value: PlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> PlaybackMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlaybackMode value: {data!r}")
    return cast(PlaybackMode, data)
