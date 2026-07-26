"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportStatus``."""

from typing import Literal, TypeAlias, cast

ExportStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
