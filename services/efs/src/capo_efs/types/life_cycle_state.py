"""Generated from Smithy shape ``com.amazonaws.efs#LifeCycleState``."""

from typing import Literal, TypeAlias, cast

LifeCycleState: TypeAlias = Literal[
    "creating",
    "available",
    "updating",
    "deleting",
    "deleted",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleState) -> str:
    return value


def deserialize_json(data: str) -> LifeCycleState:
    return cast(LifeCycleState, data)
