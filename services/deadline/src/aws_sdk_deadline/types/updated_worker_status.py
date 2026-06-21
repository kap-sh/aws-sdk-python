"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedWorkerStatus``."""

from typing import Literal, TypeAlias, cast

UpdatedWorkerStatus: TypeAlias = Literal[
    "STARTED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedWorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdatedWorkerStatus:
    return cast(UpdatedWorkerStatus, data)
