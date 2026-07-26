"""Generated from Smithy shape ``com.amazonaws.cleanrooms#WorkerComputeType``."""

from typing import Literal, TypeAlias, cast

WorkerComputeType: TypeAlias = Literal[
    "CR.1X",
    "CR.4X",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeType) -> str:
    return value


def deserialize_json(data: str) -> WorkerComputeType:
    return cast(WorkerComputeType, data)
