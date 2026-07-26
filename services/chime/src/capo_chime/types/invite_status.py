"""Generated from Smithy shape ``com.amazonaws.chime#InviteStatus``."""

from typing import Literal, TypeAlias, cast

InviteStatus: TypeAlias = Literal[
    "Pending",
    "Accepted",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: InviteStatus) -> str:
    return value


def deserialize_json(data: str) -> InviteStatus:
    return cast(InviteStatus, data)
