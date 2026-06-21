"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyStatus``."""

from typing import Literal, TypeAlias, cast

PolicyStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyStatus:
    return cast(PolicyStatus, data)
