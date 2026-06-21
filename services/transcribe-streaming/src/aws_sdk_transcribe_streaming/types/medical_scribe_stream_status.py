"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeStreamStatus``."""

from typing import Literal, TypeAlias, cast

MedicalScribeStreamStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "PAUSED",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeStreamStatus) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeStreamStatus:
    return cast(MedicalScribeStreamStatus, data)
