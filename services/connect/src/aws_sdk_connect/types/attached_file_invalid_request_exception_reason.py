"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileInvalidRequestExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AttachedFileInvalidRequestExceptionReason: TypeAlias = Literal[
    "INVALID_FILE_SIZE",
    "INVALID_FILE_TYPE",
    "INVALID_FILE_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_FILE_SIZE",
        "INVALID_FILE_TYPE",
        "INVALID_FILE_NAME",
    )
)


def serialize_json(value: AttachedFileInvalidRequestExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AttachedFileInvalidRequestExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AttachedFileInvalidRequestExceptionReason value: {data!r}"
        )
    return cast(AttachedFileInvalidRequestExceptionReason, data)
