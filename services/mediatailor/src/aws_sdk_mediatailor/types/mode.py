"""Generated from Smithy shape ``com.amazonaws.mediatailor#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

Mode: TypeAlias = Literal[
    "OFF",
    "BEHIND_LIVE_EDGE",
    "AFTER_LIVE_EDGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "BEHIND_LIVE_EDGE",
        "AFTER_LIVE_EDGE",
    )
)


def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {data!r}")
    return cast(Mode, data)
