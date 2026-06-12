"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

ExperimentReportStatus: TypeAlias = Literal[
    "pending",
    "running",
    "completed",
    "cancelled",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "running",
        "completed",
        "cancelled",
        "failed",
    )
)


def serialize_json(value: ExperimentReportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExperimentReportStatus value: {data!r}")
    return cast(ExperimentReportStatus, data)
