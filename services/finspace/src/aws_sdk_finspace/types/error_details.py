"""Generated from Smithy shape ``com.amazonaws.finspace#ErrorDetails``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

ErrorDetails: TypeAlias = Literal[
    "The inputs to this request are invalid.",
    "Service limits have been exceeded.",
    "Missing required permission to perform this request.",
    "One or more inputs to this request were not found.",
    "The system temporarily lacks sufficient resources to process the request.",
    "An internal error has occurred.",
    "Cancelled",
    "A user recoverable error has occurred",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "The inputs to this request are invalid.",
        "Service limits have been exceeded.",
        "Missing required permission to perform this request.",
        "One or more inputs to this request were not found.",
        "The system temporarily lacks sufficient resources to process the request.",
        "An internal error has occurred.",
        "Cancelled",
        "A user recoverable error has occurred",
    )
)


def serialize_json(value: ErrorDetails) -> str:
    return value


def deserialize_json(data: str) -> ErrorDetails:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorDetails value: {data!r}")
    return cast(ErrorDetails, data)
