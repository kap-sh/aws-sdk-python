"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJobStatus``."""

from typing import Literal, TypeAlias, cast

HarvestJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "CANCELLED",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestJobStatus) -> str:
    return value


def deserialize_json(data: str) -> HarvestJobStatus:
    return cast(HarvestJobStatus, data)
