"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalSpecialty``."""

from typing import Literal, TypeAlias, cast

TranscribeMedicalSpecialty: TypeAlias = Literal[
    "PRIMARYCARE",
    "CARDIOLOGY",
    "NEUROLOGY",
    "ONCOLOGY",
    "RADIOLOGY",
    "UROLOGY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeMedicalSpecialty) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalSpecialty:
    return cast(TranscribeMedicalSpecialty, data)
