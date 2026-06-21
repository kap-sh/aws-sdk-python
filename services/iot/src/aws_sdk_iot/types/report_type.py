"""Generated from Smithy shape ``com.amazonaws.iot#ReportType``."""

from typing import Literal, TypeAlias, cast

ReportType: TypeAlias = Literal[
    "ERRORS",
    "RESULTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportType) -> str:
    return value


def deserialize_json(data: str) -> ReportType:
    return cast(ReportType, data)
