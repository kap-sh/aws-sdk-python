"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PipPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

PipPosition: TypeAlias = Literal[
    "TOP_LEFT",
    "TOP_RIGHT",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOP_LEFT",
        "TOP_RIGHT",
        "BOTTOM_LEFT",
        "BOTTOM_RIGHT",
    )
)


def serialize_json(value: PipPosition) -> str:
    return value


def deserialize_json(data: str) -> PipPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipPosition value: {data!r}")
    return cast(PipPosition, data)
