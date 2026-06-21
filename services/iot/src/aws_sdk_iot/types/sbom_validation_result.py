"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationResult``."""

from typing import Literal, TypeAlias, cast

SbomValidationResult: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationResult) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationResult:
    return cast(SbomValidationResult, data)
