"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeSetState``."""

from typing import Literal, TypeAlias, cast

ChangeSetState: TypeAlias = Literal[
    "PENDING_GENERATION",
    "FAILED_GENERATION",
    "READY_TO_EXECUTE",
    "EXECUTING",
    "EXECUTION_SUCCEEDED",
    "OUT_OF_DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSetState) -> str:
    return value


def deserialize_json(data: str) -> ChangeSetState:
    return cast(ChangeSetState, data)
