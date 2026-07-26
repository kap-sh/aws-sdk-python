"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptItemType``."""

from typing import Literal, TypeAlias, cast

MedicalScribeTranscriptItemType: TypeAlias = Literal[
    "pronunciation",
    "punctuation",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptItemType) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeTranscriptItemType:
    return cast(MedicalScribeTranscriptItemType, data)
