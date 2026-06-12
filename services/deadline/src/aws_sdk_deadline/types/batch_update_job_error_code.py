"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchUpdateJobErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchUpdateJobErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateJobErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchUpdateJobErrorCode value: {data!r}")
    return cast(BatchUpdateJobErrorCode, data)
