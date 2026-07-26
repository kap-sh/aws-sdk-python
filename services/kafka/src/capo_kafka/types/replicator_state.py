"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a replicator.</p>"""
ReplicatorState: TypeAlias = Literal[
    "RUNNING",
    "CREATING",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorState) -> str:
    return value


def deserialize_json(data: str) -> ReplicatorState:
    return cast(ReplicatorState, data)
