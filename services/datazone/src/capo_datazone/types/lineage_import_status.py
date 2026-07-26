"""Generated from Smithy shape ``com.amazonaws.datazone#LineageImportStatus``."""

from typing import Literal, TypeAlias, cast

LineageImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageImportStatus) -> str:
    return value


def deserialize_json(data: str) -> LineageImportStatus:
    return cast(LineageImportStatus, data)
