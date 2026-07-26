"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorStatus``."""

from typing import Literal, TypeAlias, cast

EvaluatorStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorStatus:
    return cast(EvaluatorStatus, data)
