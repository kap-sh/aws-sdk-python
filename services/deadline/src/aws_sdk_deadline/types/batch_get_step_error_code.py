"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetStepErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetStepErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetStepErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetStepErrorCode value: {data!r}")
    return cast(BatchGetStepErrorCode, data)
