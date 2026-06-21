"""Generated from Smithy shape ``com.amazonaws.osis#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

PipelineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "STARTING",
    "START_FAILED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineStatus:
    return cast(PipelineStatus, data)
