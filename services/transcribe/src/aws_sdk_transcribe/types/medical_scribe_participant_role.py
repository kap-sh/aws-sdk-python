"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MedicalScribeParticipantRole: TypeAlias = Literal[
    "PATIENT",
    "CLINICIAN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PATIENT",
        "CLINICIAN",
    )
)


def serialize_aws_json_1_1(value: MedicalScribeParticipantRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeParticipantRole value: {data!r}"
        )
    return cast(MedicalScribeParticipantRole, data)
