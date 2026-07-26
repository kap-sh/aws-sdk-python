"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

IngestionJobStatus: TypeAlias = Literal[
    "STARTING",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobStatus:
    return cast(IngestionJobStatus, data)
