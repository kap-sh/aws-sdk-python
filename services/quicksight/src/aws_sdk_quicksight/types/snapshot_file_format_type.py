"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileFormatType``."""

from typing import Literal, TypeAlias, cast

SnapshotFileFormatType: TypeAlias = Literal[
    "CSV",
    "PDF",
    "EXCEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileFormatType) -> str:
    return value


def deserialize_json(data: str) -> SnapshotFileFormatType:
    return cast(SnapshotFileFormatType, data)
