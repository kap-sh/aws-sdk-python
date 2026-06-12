"""Generated from Smithy shape ``com.amazonaws.detective#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "INVALID_GRAPH_ARN",
    "INVALID_REQUEST_BODY",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_GRAPH_ARN",
        "INVALID_REQUEST_BODY",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
