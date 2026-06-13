"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "CONSTRAINT_VIOLATION",
    "ILLEGAL_ARGUMENT",
    "MALFORMED_QUERY",
    "QUERY_CANCELLED",
    "QUERY_TOO_LARGE",
    "UNSUPPORTED_OPERATION",
    "BAD_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONSTRAINT_VIOLATION",
        "ILLEGAL_ARGUMENT",
        "MALFORMED_QUERY",
        "QUERY_CANCELLED",
        "QUERY_TOO_LARGE",
        "UNSUPPORTED_OPERATION",
        "BAD_REQUEST",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
