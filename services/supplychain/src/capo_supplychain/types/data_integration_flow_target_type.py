"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTargetType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowTargetType: TypeAlias = Literal[
    "S3",
    "DATASET",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTargetType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowTargetType:
    return cast(DataIntegrationFlowTargetType, data)
