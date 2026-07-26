"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobWorkerComputeType``."""

from typing import Literal, TypeAlias, cast

ProtectedJobWorkerComputeType: TypeAlias = Literal[
    "CR.1X",
    "CR.4X",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobWorkerComputeType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobWorkerComputeType:
    return cast(ProtectedJobWorkerComputeType, data)
