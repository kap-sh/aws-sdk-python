"""Generated from Smithy shape ``com.amazonaws.braket#ProgramValidationFailuresList``."""

from typing import TypeAlias

ProgramValidationFailuresList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ProgramValidationFailuresList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProgramValidationFailuresList:
    return list(data)
