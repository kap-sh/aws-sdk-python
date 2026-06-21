"""Generated from Smithy shape ``com.amazonaws.deadline#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal[
    "CONFLICT_EXCEPTION",
    "CONCURRENT_MODIFICATION",
    "RESOURCE_ALREADY_EXISTS",
    "RESOURCE_IN_USE",
    "STATUS_CONFLICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
