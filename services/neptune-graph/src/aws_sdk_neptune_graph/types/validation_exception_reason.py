"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
