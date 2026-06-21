"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InvitationStatus``."""

from typing import Literal, TypeAlias, cast

InvitationStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "ACCEPTING",
    "REJECTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvitationStatus) -> str:
    return value


def deserialize_json(data: str) -> InvitationStatus:
    return cast(InvitationStatus, data)
