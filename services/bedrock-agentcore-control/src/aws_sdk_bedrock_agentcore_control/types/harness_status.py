"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessStatus``."""

from typing import Literal, TypeAlias, cast

HarnessStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessStatus) -> str:
    return value


def deserialize_json(data: str) -> HarnessStatus:
    return cast(HarnessStatus, data)
