"""Generated from Smithy shape ``com.amazonaws.connect#ContactRecordingType``."""

from typing import Literal, TypeAlias, cast

ContactRecordingType: TypeAlias = Literal[
    "AGENT",
    "IVR",
    "SCREEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactRecordingType) -> str:
    return value


def deserialize_json(data: str) -> ContactRecordingType:
    return cast(ContactRecordingType, data)
