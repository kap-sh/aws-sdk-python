"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelState``."""

from typing import Literal, TypeAlias, cast

ComputationModelState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelState) -> str:
    return value


def deserialize_json(data: str) -> ComputationModelState:
    return cast(ComputationModelState, data)
