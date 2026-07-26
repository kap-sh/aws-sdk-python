"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSetStatus``."""

from typing import Literal, TypeAlias, cast

ControlSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "UNDER_REVIEW",
    "REVIEWED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSetStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlSetStatus:
    return cast(ControlSetStatus, data)
