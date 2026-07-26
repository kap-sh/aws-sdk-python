"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationStatus``."""

from typing import Literal, TypeAlias, cast

SbomValidationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationStatus:
    return cast(SbomValidationStatus, data)
