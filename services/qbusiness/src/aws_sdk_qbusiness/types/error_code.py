"""Generated from Smithy shape ``com.amazonaws.qbusiness#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "InternalError",
    "InvalidRequest",
    "ResourceInactive",
    "ResourceNotFound",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalError",
        "InvalidRequest",
        "ResourceInactive",
        "ResourceNotFound",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
