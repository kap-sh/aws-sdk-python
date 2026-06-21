"""Generated from Smithy shape ``com.amazonaws.supplychain#InstanceState``."""

from typing import Literal, TypeAlias, cast

InstanceState: TypeAlias = Literal[
    "Initializing",
    "Active",
    "CreateFailed",
    "DeleteFailed",
    "Deleting",
    "Deleted",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceState) -> str:
    return value


def deserialize_json(data: str) -> InstanceState:
    return cast(InstanceState, data)
