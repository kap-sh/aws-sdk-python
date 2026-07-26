"""Generated from Smithy shape ``com.amazonaws.inspector2#CisReportFormat``."""

from typing import Literal, TypeAlias, cast

CisReportFormat: TypeAlias = Literal[
    "PDF",
    "CSV",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisReportFormat) -> str:
    return value


def deserialize_json(data: str) -> CisReportFormat:
    return cast(CisReportFormat, data)
