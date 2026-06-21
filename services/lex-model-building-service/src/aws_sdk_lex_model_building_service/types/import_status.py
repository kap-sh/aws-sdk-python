"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
