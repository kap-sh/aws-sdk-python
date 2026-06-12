"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetTaskErrorCode: TypeAlias = Literal[
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalServerErrorException",
        "ResourceNotFoundException",
        "ValidationException",
        "AccessDeniedException",
        "ThrottlingException",
    )
)


def serialize_json(value: BatchGetTaskErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetTaskErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetTaskErrorCode value: {data!r}")
    return cast(BatchGetTaskErrorCode, data)
