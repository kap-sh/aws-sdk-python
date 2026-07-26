"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetWorkerErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetWorkerErrorCode:
    return cast(BatchGetWorkerErrorCode, data)
