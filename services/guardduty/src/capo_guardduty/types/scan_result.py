"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResult``."""

from typing import Literal, TypeAlias, cast

ScanResult: TypeAlias = Literal[
    "CLEAN",
    "INFECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResult) -> str:
    return value


def deserialize_json(data: str) -> ScanResult:
    return cast(ScanResult, data)
