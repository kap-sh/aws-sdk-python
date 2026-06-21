"""Generated from Smithy shape ``com.amazonaws.novaact#ActStatus``."""

from typing import Literal, TypeAlias, cast

ActStatus: TypeAlias = Literal[
    "RUNNING",
    "PENDING_CLIENT_ACTION",
    "PENDING_HUMAN_ACTION",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActStatus) -> str:
    return value


def deserialize_json(data: str) -> ActStatus:
    return cast(ActStatus, data)
