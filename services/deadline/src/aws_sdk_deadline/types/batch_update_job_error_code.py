"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchUpdateJobErrorCode: TypeAlias = Literal[
    "ConflictException",
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateJobErrorCode:
    return cast(BatchUpdateJobErrorCode, data)
