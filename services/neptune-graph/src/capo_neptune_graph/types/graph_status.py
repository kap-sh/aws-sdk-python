"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphStatus``."""

from typing import Literal, TypeAlias, cast

GraphStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "RESETTING",
    "UPDATING",
    "SNAPSHOTTING",
    "FAILED",
    "IMPORTING",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphStatus) -> str:
    return value


def deserialize_json(data: str) -> GraphStatus:
    return cast(GraphStatus, data)
