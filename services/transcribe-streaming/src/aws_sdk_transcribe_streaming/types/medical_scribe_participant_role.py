"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalScribeParticipantRole: TypeAlias = Literal[
    "PATIENT",
    "CLINICIAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PATIENT",
        "CLINICIAN",
    )
)


def serialize_json(value: MedicalScribeParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeParticipantRole value: {data!r}"
        )
    return cast(MedicalScribeParticipantRole, data)
