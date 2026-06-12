"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetSessionErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetSessionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetSessionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetSessionErrorCode value: {data!r}")
    return cast(BatchGetSessionErrorCode, data)
