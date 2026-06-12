"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetJobErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetJobErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetJobErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetJobErrorCode value: {data!r}")
    return cast(BatchGetJobErrorCode, data)
