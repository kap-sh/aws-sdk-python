"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportTaskStatus``."""

from typing import Literal, TypeAlias, cast

ImportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "INITIALIZED",
    "PENDING",
    "COMPLETE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportTaskStatus:
    return cast(ImportTaskStatus, data)
