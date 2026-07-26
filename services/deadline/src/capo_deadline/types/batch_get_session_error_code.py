"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetSessionErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetSessionErrorCode:
    return cast(BatchGetSessionErrorCode, data)
