"""Generated from Smithy shape ``com.amazonaws.deadline#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

ConflictExceptionReason: TypeAlias = Literal[
    "CONFLICT_EXCEPTION",
    "CONCURRENT_MODIFICATION",
    "RESOURCE_ALREADY_EXISTS",
    "RESOURCE_IN_USE",
    "STATUS_CONFLICT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFLICT_EXCEPTION",
        "CONCURRENT_MODIFICATION",
        "RESOURCE_ALREADY_EXISTS",
        "RESOURCE_IN_USE",
        "STATUS_CONFLICT",
    )
)


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
