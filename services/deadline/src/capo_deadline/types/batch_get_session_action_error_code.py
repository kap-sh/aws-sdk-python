"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetSessionActionErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetSessionActionErrorCode:
    return cast(BatchGetSessionActionErrorCode, data)
