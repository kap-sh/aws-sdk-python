"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "DUPLICATE_IDENTIFIER",
    "ITEM_DOES_NOT_EXIST",
    "INTERNAL_ERROR",
    "INVALID_FINDING_ID",
    "INVALID_SCAN_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_IDENTIFIER",
        "ITEM_DOES_NOT_EXIST",
        "INTERNAL_ERROR",
        "INVALID_FINDING_ID",
        "INVALID_SCAN_NAME",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
