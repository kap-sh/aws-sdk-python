"""Generated from Smithy shape ``com.amazonaws.finspacedata#ErrorCategory``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ErrorCategory) -> str:
    return value


def deserialize_json(data: str) -> ErrorCategory:
    return cast(ErrorCategory, data)
