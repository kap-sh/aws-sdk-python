"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ClinicalNoteGenerationStatus``."""

from typing import Literal, TypeAlias, cast

ClinicalNoteGenerationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> ClinicalNoteGenerationStatus:
    return cast(ClinicalNoteGenerationStatus, data)
