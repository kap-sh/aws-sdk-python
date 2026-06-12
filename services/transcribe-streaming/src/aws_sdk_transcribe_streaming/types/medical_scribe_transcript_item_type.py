"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalScribeTranscriptItemType: TypeAlias = Literal[
    "pronunciation",
    "punctuation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pronunciation",
        "punctuation",
    )
)


def serialize_json(value: MedicalScribeTranscriptItemType) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeTranscriptItemType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeTranscriptItemType value: {data!r}"
        )
    return cast(MedicalScribeTranscriptItemType, data)
