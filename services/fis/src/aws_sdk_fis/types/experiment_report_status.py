"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportStatus``."""

from typing import Literal, TypeAlias, cast

ExperimentReportStatus: TypeAlias = Literal[
    "pending",
    "running",
    "completed",
    "cancelled",
    "failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentReportStatus:
    return cast(ExperimentReportStatus, data)
