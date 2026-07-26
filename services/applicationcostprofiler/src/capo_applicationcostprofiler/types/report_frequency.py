"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportFrequency``."""

from typing import Literal, TypeAlias, cast

ReportFrequency: TypeAlias = Literal[
    "MONTHLY",
    "DAILY",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportFrequency) -> str:
    return value


def deserialize_json(data: str) -> ReportFrequency:
    return cast(ReportFrequency, data)
