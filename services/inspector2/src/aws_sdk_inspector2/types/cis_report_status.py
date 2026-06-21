"""Generated from Smithy shape ``com.amazonaws.inspector2#CisReportStatus``."""

from typing import Literal, TypeAlias, cast

CisReportStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisReportStatus) -> str:
    return value


def deserialize_json(data: str) -> CisReportStatus:
    return cast(CisReportStatus, data)
