"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeNoteTemplate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MedicalScribeNoteTemplate: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "BIRP",
    "SIRP",
    "DAP",
    "BEHAVIORAL_SOAP",
    "PHYSICAL_SOAP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HISTORY_AND_PHYSICAL",
        "GIRPP",
        "BIRP",
        "SIRP",
        "DAP",
        "BEHAVIORAL_SOAP",
        "PHYSICAL_SOAP",
    )
)


def serialize_aws_json_1_1(value: MedicalScribeNoteTemplate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeNoteTemplate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MedicalScribeNoteTemplate value: {data!r}")
    return cast(MedicalScribeNoteTemplate, data)
