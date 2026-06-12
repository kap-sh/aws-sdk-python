"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

UnprocessedErrorCode: TypeAlias = Literal[
    "INVALID_INPUT",
    "ACCESS_DENIED",
    "NOT_FOUND",
    "RESOURCE_NOT_FOUND",
    "LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_INPUT",
        "ACCESS_DENIED",
        "NOT_FOUND",
        "RESOURCE_NOT_FOUND",
        "LIMIT_EXCEEDED",
    )
)


def serialize_json(value: UnprocessedErrorCode) -> str:
    return value


def deserialize_json(data: str) -> UnprocessedErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnprocessedErrorCode value: {data!r}")
    return cast(UnprocessedErrorCode, data)
