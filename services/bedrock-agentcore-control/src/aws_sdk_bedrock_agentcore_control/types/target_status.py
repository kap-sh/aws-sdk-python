"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetStatus``."""

from typing import Literal, TypeAlias, cast

TargetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "UPDATE_UNSUCCESSFUL",
    "DELETING",
    "READY",
    "FAILED",
    "SYNCHRONIZING",
    "SYNCHRONIZE_UNSUCCESSFUL",
    "CREATE_PENDING_AUTH",
    "UPDATE_PENDING_AUTH",
    "SYNCHRONIZE_PENDING_AUTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetStatus:
    return cast(TargetStatus, data)
