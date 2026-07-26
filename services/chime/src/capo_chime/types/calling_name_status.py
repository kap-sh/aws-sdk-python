"""Generated from Smithy shape ``com.amazonaws.chime#CallingNameStatus``."""

from typing import Literal, TypeAlias, cast

CallingNameStatus: TypeAlias = Literal[
    "Unassigned",
    "UpdateInProgress",
    "UpdateSucceeded",
    "UpdateFailed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CallingNameStatus) -> str:
    return value


def deserialize_json(data: str) -> CallingNameStatus:
    return cast(CallingNameStatus, data)
