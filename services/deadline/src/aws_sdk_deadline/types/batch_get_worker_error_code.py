"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetWorkerErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalServerErrorException",
        "ResourceNotFoundException",
        "ValidationException",
    )
)


def serialize_json(value: BatchGetWorkerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetWorkerErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetWorkerErrorCode value: {data!r}")
    return cast(BatchGetWorkerErrorCode, data)
