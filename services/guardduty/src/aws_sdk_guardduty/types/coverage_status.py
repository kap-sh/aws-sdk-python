"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatus``."""

from typing import Literal, TypeAlias, cast

CoverageStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatus) -> str:
    return value


def deserialize_json(data: str) -> CoverageStatus:
    return cast(CoverageStatus, data)
