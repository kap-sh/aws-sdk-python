"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunStatus``."""

from typing import Literal, TypeAlias, cast

MetadataGenerationRunStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "CANCELED",
    "SUCCEEDED",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunStatus) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationRunStatus:
    return cast(MetadataGenerationRunStatus, data)
