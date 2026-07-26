"""Generated from Smithy shape ``com.amazonaws.neptunegraph#UnprocessableExceptionReason``."""

from typing import Literal, TypeAlias, cast

UnprocessableExceptionReason: TypeAlias = Literal[
    "QUERY_TIMEOUT",
    "INTERNAL_LIMIT_EXCEEDED",
    "MEMORY_LIMIT_EXCEEDED",
    "STORAGE_LIMIT_EXCEEDED",
    "PARTITION_FULL",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> UnprocessableExceptionReason:
    return cast(UnprocessableExceptionReason, data)
