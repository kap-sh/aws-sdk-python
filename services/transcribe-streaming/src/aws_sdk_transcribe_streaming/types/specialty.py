"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Specialty``."""

from typing import Literal, TypeAlias, cast

Specialty: TypeAlias = Literal[
    "PRIMARYCARE",
    "CARDIOLOGY",
    "NEUROLOGY",
    "ONCOLOGY",
    "RADIOLOGY",
    "UROLOGY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Specialty) -> str:
    return value


def deserialize_json(data: str) -> Specialty:
    return cast(Specialty, data)
