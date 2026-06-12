"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEbpPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Ebp Placement"""
M2tsEbpPlacement: TypeAlias = Literal[
    "VIDEO_AND_AUDIO_PIDS",
    "VIDEO_PID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIDEO_AND_AUDIO_PIDS",
        "VIDEO_PID",
    )
)


def serialize_json(value: M2tsEbpPlacement) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbpPlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsEbpPlacement value: {data!r}")
    return cast(M2tsEbpPlacement, data)
