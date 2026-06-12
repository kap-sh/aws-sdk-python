"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeMedicalType: TypeAlias = Literal[
    "CONVERSATION",
    "DICTATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONVERSATION",
        "DICTATION",
    )
)


def serialize_json(value: TranscribeMedicalType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscribeMedicalType value: {data!r}")
    return cast(TranscribeMedicalType, data)
