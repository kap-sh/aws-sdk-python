"""Generated from Smithy shape ``com.amazonaws.connect#ContactState``."""

from typing import Literal, TypeAlias, cast

ContactState: TypeAlias = Literal[
    "INCOMING",
    "PENDING",
    "CONNECTING",
    "CONNECTED",
    "CONNECTED_ONHOLD",
    "MISSED",
    "ERROR",
    "ENDED",
    "REJECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactState) -> str:
    return value


def deserialize_json(data: str) -> ContactState:
    return cast(ContactState, data)
