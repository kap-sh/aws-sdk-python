"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskStatus``."""

from typing import Literal, TypeAlias, cast

ImportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "EXPORTING",
    "ANALYZING_DATA",
    "IMPORTING",
    "REPROVISIONING",
    "ROLLING_BACK",
    "SUCCEEDED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportTaskStatus:
    return cast(ImportTaskStatus, data)
