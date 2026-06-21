"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlStatus``."""

from typing import Literal, TypeAlias, cast

ControlStatus: TypeAlias = Literal[
    "UNDER_REVIEW",
    "REVIEWED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlStatus:
    return cast(ControlStatus, data)
