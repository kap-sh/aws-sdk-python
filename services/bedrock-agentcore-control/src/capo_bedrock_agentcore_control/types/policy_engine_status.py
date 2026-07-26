"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngineStatus``."""

from typing import Literal, TypeAlias, cast

PolicyEngineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEngineStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyEngineStatus:
    return cast(PolicyEngineStatus, data)
