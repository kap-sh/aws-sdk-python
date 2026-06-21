"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeStatus``."""

from typing import Literal, TypeAlias, cast

ChangeStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeStatus:
    return cast(ChangeStatus, data)
