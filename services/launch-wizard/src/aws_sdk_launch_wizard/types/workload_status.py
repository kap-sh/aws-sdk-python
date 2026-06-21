"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadStatus``."""

from typing import Literal, TypeAlias, cast

WorkloadStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadStatus:
    return cast(WorkloadStatus, data)
