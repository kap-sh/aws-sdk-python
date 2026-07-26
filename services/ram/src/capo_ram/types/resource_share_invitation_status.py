"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationStatus``."""

from typing import Literal, TypeAlias, cast

ResourceShareInvitationStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareInvitationStatus:
    return cast(ResourceShareInvitationStatus, data)
