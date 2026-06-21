"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatus``."""

from typing import Literal, TypeAlias, cast

CisScanStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
    "CANCELLED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanStatus) -> str:
    return value


def deserialize_json(data: str) -> CisScanStatus:
    return cast(CisScanStatus, data)
