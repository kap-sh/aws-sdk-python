"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetOperationType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationEventDatasetOperationType: TypeAlias = Literal[
    "APPEND",
    "UPSERT",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetOperationType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationEventDatasetOperationType:
    return cast(DataIntegrationEventDatasetOperationType, data)
