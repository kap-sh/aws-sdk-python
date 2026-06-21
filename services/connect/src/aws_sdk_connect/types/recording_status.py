"""Generated from Smithy shape ``com.amazonaws.connect#RecordingStatus``."""

from typing import Literal, TypeAlias, cast

RecordingStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordingStatus) -> str:
    return value


def deserialize_json(data: str) -> RecordingStatus:
    return cast(RecordingStatus, data)
