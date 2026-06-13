"""Generated from Smithy shape ``com.amazonaws.neptunegraph#UnprocessableExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

UnprocessableExceptionReason: TypeAlias = Literal[
    "QUERY_TIMEOUT",
    "INTERNAL_LIMIT_EXCEEDED",
    "MEMORY_LIMIT_EXCEEDED",
    "STORAGE_LIMIT_EXCEEDED",
    "PARTITION_FULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUERY_TIMEOUT",
        "INTERNAL_LIMIT_EXCEEDED",
        "MEMORY_LIMIT_EXCEEDED",
        "STORAGE_LIMIT_EXCEEDED",
        "PARTITION_FULL",
    )
)


def serialize_json(value: UnprocessableExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> UnprocessableExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UnprocessableExceptionReason value: {data!r}"
        )
    return cast(UnprocessableExceptionReason, data)
