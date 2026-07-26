"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchUpdateTaskErrorCode: TypeAlias = Literal[
    "ConflictException",
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateTaskErrorCode:
    return cast(BatchUpdateTaskErrorCode, data)
