"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalType``."""

from typing import Literal, TypeAlias, cast

TranscribeMedicalType: TypeAlias = Literal[
    "CONVERSATION",
    "DICTATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeMedicalType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalType:
    return cast(TranscribeMedicalType, data)
