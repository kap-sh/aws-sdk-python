"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanType``."""

from typing import Literal, TypeAlias, cast

ScanType: TypeAlias = Literal[
    "Standard",
    "Express",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanType) -> str:
    return value


def deserialize_json(data: str) -> ScanType:
    return cast(ScanType, data)
