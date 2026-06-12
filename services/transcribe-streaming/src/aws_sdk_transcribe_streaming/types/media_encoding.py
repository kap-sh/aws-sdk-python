"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MediaEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MediaEncoding: TypeAlias = Literal[
    "pcm",
    "ogg-opus",
    "flac",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pcm",
        "ogg-opus",
        "flac",
    )
)


def serialize_json(value: MediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MediaEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaEncoding value: {data!r}")
    return cast(MediaEncoding, data)
