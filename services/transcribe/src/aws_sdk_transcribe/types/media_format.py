"""Generated from Smithy shape ``com.amazonaws.transcribe#MediaFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MediaFormat: TypeAlias = Literal[
    "mp3",
    "mp4",
    "wav",
    "flac",
    "ogg",
    "amr",
    "webm",
    "m4a",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "mp3",
        "mp4",
        "wav",
        "flac",
        "ogg",
        "amr",
        "webm",
        "m4a",
    )
)


def serialize_aws_json_1_1(value: MediaFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MediaFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaFormat value: {data!r}")
    return cast(MediaFormat, data)
