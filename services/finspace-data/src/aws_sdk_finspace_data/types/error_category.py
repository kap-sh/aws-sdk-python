"""Generated from Smithy shape ``com.amazonaws.finspacedata#ErrorCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Changeset Error Category"""
ErrorCategory: TypeAlias = Literal[
    "VALIDATION",
    "SERVICE_QUOTA_EXCEEDED",
    "ACCESS_DENIED",
    "RESOURCE_NOT_FOUND",
    "THROTTLING",
    "INTERNAL_SERVICE_EXCEPTION",
    "CANCELLED",
    "USER_RECOVERABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATION",
        "SERVICE_QUOTA_EXCEEDED",
        "ACCESS_DENIED",
        "RESOURCE_NOT_FOUND",
        "THROTTLING",
        "INTERNAL_SERVICE_EXCEPTION",
        "CANCELLED",
        "USER_RECOVERABLE",
    )
)


def serialize_json(value: ErrorCategory) -> str:
    return value


def deserialize_json(data: str) -> ErrorCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCategory value: {data!r}")
    return cast(ErrorCategory, data)
