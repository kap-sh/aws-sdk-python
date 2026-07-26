"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ExportStatus``."""

from typing import Literal, TypeAlias, cast

ExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
