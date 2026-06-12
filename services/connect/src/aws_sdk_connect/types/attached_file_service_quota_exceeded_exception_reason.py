"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AttachedFileServiceQuotaExceededExceptionReason: TypeAlias = Literal[
    "TOTAL_FILE_SIZE_EXCEEDED",
    "TOTAL_FILE_COUNT_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOTAL_FILE_SIZE_EXCEEDED",
        "TOTAL_FILE_COUNT_EXCEEDED",
    )
)


def serialize_json(value: AttachedFileServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AttachedFileServiceQuotaExceededExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AttachedFileServiceQuotaExceededExceptionReason value: {data!r}"
        )
    return cast(AttachedFileServiceQuotaExceededExceptionReason, data)
