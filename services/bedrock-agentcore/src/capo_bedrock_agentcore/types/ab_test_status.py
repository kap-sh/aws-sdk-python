"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestStatus``."""

from typing import Literal, TypeAlias, cast

ABTestStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ABTestStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestStatus:
    return cast(ABTestStatus, data)
