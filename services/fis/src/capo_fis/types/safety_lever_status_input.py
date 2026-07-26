"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLeverStatusInput``."""

from typing import Literal, TypeAlias, cast

SafetyLeverStatusInput: TypeAlias = Literal[
    "disengaged",
    "engaged",
]


# --- restJson1 ser/de ---
def serialize_json(value: SafetyLeverStatusInput) -> str:
    return value


def deserialize_json(data: str) -> SafetyLeverStatusInput:
    return cast(SafetyLeverStatusInput, data)
