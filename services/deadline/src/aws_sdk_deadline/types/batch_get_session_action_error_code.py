"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BatchGetSessionActionErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetSessionActionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetSessionActionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchGetSessionActionErrorCode value: {data!r}"
        )
    return cast(BatchGetSessionActionErrorCode, data)
