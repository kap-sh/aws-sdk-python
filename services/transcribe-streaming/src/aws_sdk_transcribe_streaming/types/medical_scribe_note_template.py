"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeNoteTemplate``."""

from typing import Literal, TypeAlias, cast

MedicalScribeNoteTemplate: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "DAP",
    "SIRP",
    "BIRP",
    "BEHAVIORAL_SOAP",
    "PHYSICAL_SOAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeNoteTemplate) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeNoteTemplate:
    return cast(MedicalScribeNoteTemplate, data)
