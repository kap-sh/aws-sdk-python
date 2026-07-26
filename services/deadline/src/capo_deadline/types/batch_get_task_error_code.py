"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetTaskErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetTaskErrorCode:
    return cast(BatchGetTaskErrorCode, data)
