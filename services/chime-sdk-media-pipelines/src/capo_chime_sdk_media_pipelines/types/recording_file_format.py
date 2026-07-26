"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RecordingFileFormat``."""

from typing import Literal, TypeAlias, cast

RecordingFileFormat: TypeAlias = Literal[
    "Wav",
    "Opus",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordingFileFormat) -> str:
    return value


def deserialize_json(data: str) -> RecordingFileFormat:
    return cast(RecordingFileFormat, data)
