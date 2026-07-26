"""Generated from Smithy shape ``com.amazonaws.controltower#DriftStatus``."""

from typing import Literal, TypeAlias, cast

DriftStatus: TypeAlias = Literal[
    "DRIFTED",
    "IN_SYNC",
    "NOT_CHECKING",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DriftStatus) -> str:
    return value


def deserialize_json(data: str) -> DriftStatus:
    return cast(DriftStatus, data)
