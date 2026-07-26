"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamStatus``."""

from typing import Literal, TypeAlias, cast

ApprovalTeamStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETING",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalTeamStatus) -> str:
    return value


def deserialize_json(data: str) -> ApprovalTeamStatus:
    return cast(ApprovalTeamStatus, data)
