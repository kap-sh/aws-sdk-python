"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RecordingFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

RecordingFileFormat: TypeAlias = Literal[
    "Wav",
    "Opus",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Wav",
        "Opus",
    )
)


def serialize_json(value: RecordingFileFormat) -> str:
    return value


def deserialize_json(data: str) -> RecordingFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordingFileFormat value: {data!r}")
    return cast(RecordingFileFormat, data)
