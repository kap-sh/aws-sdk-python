"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "DUPLICATE_IDENTIFIER",
    "ITEM_DOES_NOT_EXIST",
    "INTERNAL_ERROR",
    "INVALID_FINDING_ID",
    "INVALID_SCAN_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
