"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetLoadStatus``."""

from typing import Literal, TypeAlias, cast

DataIntegrationEventDatasetLoadStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetLoadStatus) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationEventDatasetLoadStatus:
    return cast(DataIntegrationEventDatasetLoadStatus, data)
