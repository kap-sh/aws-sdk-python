"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Specialty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

Specialty: TypeAlias = Literal[
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


def serialize_json(value: Specialty) -> str:
    return value


def deserialize_json(data: str) -> Specialty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Specialty value: {data!r}")
    return cast(Specialty, data)
