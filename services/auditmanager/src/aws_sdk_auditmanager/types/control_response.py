"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlResponse``."""

from typing import Literal, TypeAlias, cast

ControlResponse: TypeAlias = Literal[
    "MANUAL",
    "AUTOMATE",
    "DEFER",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlResponse) -> str:
    return value


def deserialize_json(data: str) -> ControlResponse:
    return cast(ControlResponse, data)
