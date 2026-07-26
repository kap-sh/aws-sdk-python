"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionStatus``."""

from typing import Literal, TypeAlias, cast

ExperimentActionStatus: TypeAlias = Literal[
    "pending",
    "initiating",
    "running",
    "completed",
    "cancelled",
    "stopping",
    "stopped",
    "failed",
    "skipped",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentActionStatus:
    return cast(ExperimentActionStatus, data)
