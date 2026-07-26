"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserStatus``."""

from typing import Literal, TypeAlias, cast

BrowserStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserStatus:
    return cast(BrowserStatus, data)
