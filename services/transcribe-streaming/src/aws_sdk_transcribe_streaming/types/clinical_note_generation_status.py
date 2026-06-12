"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ClinicalNoteGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ClinicalNoteGenerationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: ClinicalNoteGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> ClinicalNoteGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClinicalNoteGenerationStatus value: {data!r}"
        )
    return cast(ClinicalNoteGenerationStatus, data)
