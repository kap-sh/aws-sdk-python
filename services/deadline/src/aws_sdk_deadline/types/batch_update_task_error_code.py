"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchUpdateTaskErrorCode: TypeAlias = Literal[
    "ConflictException",
    "InternalServerErrorException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConflictException",
        "InternalServerErrorException",
        "ResourceNotFoundException",
        "ValidationException",
        "AccessDeniedException",
        "ThrottlingException",
    )
)


def serialize_json(value: BatchUpdateTaskErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateTaskErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchUpdateTaskErrorCode value: {data!r}")
    return cast(BatchUpdateTaskErrorCode, data)
