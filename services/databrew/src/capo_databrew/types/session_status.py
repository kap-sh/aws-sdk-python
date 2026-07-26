"""Generated from Smithy shape ``com.amazonaws.databrew#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "ASSIGNED",
    "FAILED",
    "INITIALIZING",
    "PROVISIONING",
    "READY",
    "RECYCLING",
    "ROTATING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
