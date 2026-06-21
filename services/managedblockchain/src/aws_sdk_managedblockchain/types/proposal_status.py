"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalStatus``."""

from typing import Literal, TypeAlias, cast

ProposalStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "APPROVED",
    "REJECTED",
    "EXPIRED",
    "ACTION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProposalStatus) -> str:
    return value


def deserialize_json(data: str) -> ProposalStatus:
    return cast(ProposalStatus, data)
