"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationConfigStatus``."""

from typing import Literal, TypeAlias, cast

OnlineEvaluationConfigStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationConfigStatus) -> str:
    return value


def deserialize_json(data: str) -> OnlineEvaluationConfigStatus:
    return cast(OnlineEvaluationConfigStatus, data)
