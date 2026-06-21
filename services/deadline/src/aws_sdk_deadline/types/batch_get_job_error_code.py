"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetJobErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetJobErrorCode:
    return cast(BatchGetJobErrorCode, data)
