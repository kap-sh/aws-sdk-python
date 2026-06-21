"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanStatus``."""

from typing import Literal, TypeAlias, cast

ScanStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanStatus:
    return cast(ScanStatus, data)
