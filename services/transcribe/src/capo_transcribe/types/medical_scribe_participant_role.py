"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeParticipantRole``."""

from typing import Literal, TypeAlias, cast

MedicalScribeParticipantRole: TypeAlias = Literal[
    "PATIENT",
    "CLINICIAN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeParticipantRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeParticipantRole:
    return cast(MedicalScribeParticipantRole, data)
