"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

AudioFormat: TypeAlias = Literal[
    "mp3",
    "opus",
    "wav",
    "aac",
    "flac",
    "mp4",
    "ogg",
    "mkv",
    "mka",
    "x-aac",
    "m4a",
    "mpeg",
    "mpga",
    "pcm",
    "webm",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "mp3",
        "opus",
        "wav",
        "aac",
        "flac",
        "mp4",
        "ogg",
        "mkv",
        "mka",
        "x-aac",
        "m4a",
        "mpeg",
        "mpga",
        "pcm",
        "webm",
    )
)


def serialize_json(value: AudioFormat) -> str:
    return value


def deserialize_json(data: str) -> AudioFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioFormat value: {data!r}")
    return cast(AudioFormat, data)
