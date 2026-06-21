"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCategory``."""

from typing import Literal, TypeAlias, cast

ScanCategory: TypeAlias = Literal[
    "FULL_SCAN",
    "INCREMENTAL_SCAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanCategory) -> str:
    return value


def deserialize_json(data: str) -> ScanCategory:
    return cast(ScanCategory, data)
