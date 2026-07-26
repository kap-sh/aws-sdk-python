"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanState``."""

from typing import Literal, TypeAlias, cast

ScanState: TypeAlias = Literal[
    "InProgress",
    "Successful",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanState) -> str:
    return value


def deserialize_json(data: str) -> ScanState:
    return cast(ScanState, data)
