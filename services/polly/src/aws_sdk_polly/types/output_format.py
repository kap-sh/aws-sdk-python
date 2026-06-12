"""Generated from Smithy shape ``com.amazonaws.polly#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "json",
    "mp3",
    "ogg_opus",
    "ogg_vorbis",
    "pcm",
    "mulaw",
    "alaw",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "mp3",
        "ogg_opus",
        "ogg_vorbis",
        "pcm",
        "mulaw",
        "alaw",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
