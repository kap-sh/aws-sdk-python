"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeSessionControlEventType``."""

from typing import Literal, TypeAlias, cast

MedicalScribeSessionControlEventType: TypeAlias = Literal["END_OF_SESSION",]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeSessionControlEventType) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeSessionControlEventType:
    return cast(MedicalScribeSessionControlEventType, data)
