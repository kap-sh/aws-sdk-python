"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationErrorCode``."""

from typing import Literal, TypeAlias, cast

SbomValidationErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_FORMAT",
    "FILE_SIZE_LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationErrorCode) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationErrorCode:
    return cast(SbomValidationErrorCode, data)
