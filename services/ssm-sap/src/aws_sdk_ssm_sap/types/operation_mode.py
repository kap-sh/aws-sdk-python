"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationMode``."""

from typing import Literal, TypeAlias, cast

OperationMode: TypeAlias = Literal[
    "PRIMARY",
    "LOGREPLAY",
    "DELTA_DATASHIPPING",
    "LOGREPLAY_READACCESS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationMode) -> str:
    return value


def deserialize_json(data: str) -> OperationMode:
    return cast(OperationMode, data)
