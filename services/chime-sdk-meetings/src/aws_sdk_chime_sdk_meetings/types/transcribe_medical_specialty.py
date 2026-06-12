"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalSpecialty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeMedicalSpecialty: TypeAlias = Literal[
    "PRIMARYCARE",
    "CARDIOLOGY",
    "NEUROLOGY",
    "ONCOLOGY",
    "RADIOLOGY",
    "UROLOGY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARYCARE",
        "CARDIOLOGY",
        "NEUROLOGY",
        "ONCOLOGY",
        "RADIOLOGY",
        "UROLOGY",
    )
)


def serialize_json(value: TranscribeMedicalSpecialty) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalSpecialty:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeMedicalSpecialty value: {data!r}"
        )
    return cast(TranscribeMedicalSpecialty, data)
