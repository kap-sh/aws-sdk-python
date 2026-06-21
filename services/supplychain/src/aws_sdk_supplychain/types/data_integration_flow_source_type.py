"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSourceType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowSourceType: TypeAlias = Literal[
    "S3",
    "DATASET",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowSourceType:
    return cast(DataIntegrationFlowSourceType, data)
