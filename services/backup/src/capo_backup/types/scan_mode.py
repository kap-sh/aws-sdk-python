"""Generated from Smithy shape ``com.amazonaws.backup#ScanMode``."""

from typing import Literal, TypeAlias, cast

ScanMode: TypeAlias = Literal[
    "FULL_SCAN",
    "INCREMENTAL_SCAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanMode) -> str:
    return value


def deserialize_json(data: str) -> ScanMode:
    return cast(ScanMode, data)
