"""Generated from Smithy shape ``com.amazonaws.connecthealth#ManagedNoteTemplate``."""

from typing import Literal, TypeAlias, cast

ManagedNoteTemplate: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "DAP",
    "SIRP",
    "BIRP",
    "BEHAVIORAL_SOAP",
    "PHYSICAL_SOAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNoteTemplate) -> str:
    return value


def deserialize_json(data: str) -> ManagedNoteTemplate:
    return cast(ManagedNoteTemplate, data)
