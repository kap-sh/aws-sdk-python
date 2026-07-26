"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

AttachedFileServiceQuotaExceededExceptionReason: TypeAlias = Literal[
    "TOTAL_FILE_SIZE_EXCEEDED",
    "TOTAL_FILE_COUNT_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFileServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AttachedFileServiceQuotaExceededExceptionReason:
    return cast(AttachedFileServiceQuotaExceededExceptionReason, data)
