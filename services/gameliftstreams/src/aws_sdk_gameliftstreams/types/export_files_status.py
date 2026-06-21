"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ExportFilesStatus``."""

from typing import Literal, TypeAlias, cast

ExportFilesStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilesStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportFilesStatus:
    return cast(ExportFilesStatus, data)
