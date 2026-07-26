"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatus``."""

from typing import Literal, TypeAlias, cast

CisFindingStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisFindingStatus) -> str:
    return value


def deserialize_json(data: str) -> CisFindingStatus:
    return cast(CisFindingStatus, data)
