"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentStatus``."""

from typing import Literal, TypeAlias, cast

ExperimentStatus: TypeAlias = Literal[
    "pending",
    "initiating",
    "running",
    "completed",
    "stopping",
    "stopped",
    "failed",
    "cancelled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentStatus:
    return cast(ExperimentStatus, data)
