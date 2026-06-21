"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
