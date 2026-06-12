"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M3u8NielsenId3``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
M3u8NielsenId3: TypeAlias = Literal[
    "INSERT",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "NONE",
    )
)


def serialize_json(value: M3u8NielsenId3) -> str:
    return value


def deserialize_json(data: str) -> M3u8NielsenId3:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M3u8NielsenId3 value: {data!r}")
    return cast(M3u8NielsenId3, data)
