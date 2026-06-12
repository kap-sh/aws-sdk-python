"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntityErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

JobEntityErrorCode: TypeAlias = Literal[
    "AccessDeniedException",
    "InternalServerException",
    "ValidationException",
    "ResourceNotFoundException",
    "MaxPayloadSizeExceeded",
    "ConflictException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessDeniedException",
        "InternalServerException",
        "ValidationException",
        "ResourceNotFoundException",
        "MaxPayloadSizeExceeded",
        "ConflictException",
    )
)


def serialize_json(value: JobEntityErrorCode) -> str:
    return value


def deserialize_json(data: str) -> JobEntityErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobEntityErrorCode value: {data!r}")
    return cast(JobEntityErrorCode, data)
