"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskStatus``."""

from typing import Literal, TypeAlias, cast

ExportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "EXPORTING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportTaskStatus:
    return cast(ExportTaskStatus, data)
