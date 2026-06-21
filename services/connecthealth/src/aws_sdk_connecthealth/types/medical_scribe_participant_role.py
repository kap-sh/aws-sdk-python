"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeParticipantRole``."""

from typing import Literal, TypeAlias, cast

MedicalScribeParticipantRole: TypeAlias = Literal[
    "PATIENT",
    "CLINICIAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeParticipantRole:
    return cast(MedicalScribeParticipantRole, data)
