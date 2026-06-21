"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetStepErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetStepErrorCode:
    return cast(BatchGetStepErrorCode, data)
