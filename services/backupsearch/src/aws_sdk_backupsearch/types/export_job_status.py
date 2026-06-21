"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportJobStatus``."""

from typing import Literal, TypeAlias, cast

ExportJobStatus: TypeAlias = Literal[
    "RUNNING",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportJobStatus:
    return cast(ExportJobStatus, data)
