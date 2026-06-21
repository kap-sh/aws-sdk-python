"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileInvalidRequestExceptionReason``."""

from typing import Literal, TypeAlias, cast

AttachedFileInvalidRequestExceptionReason: TypeAlias = Literal[
    "INVALID_FILE_SIZE",
    "INVALID_FILE_TYPE",
    "INVALID_FILE_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFileInvalidRequestExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AttachedFileInvalidRequestExceptionReason:
    return cast(AttachedFileInvalidRequestExceptionReason, data)
