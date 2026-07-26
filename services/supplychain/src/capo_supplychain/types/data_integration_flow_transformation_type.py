"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTransformationType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowTransformationType: TypeAlias = Literal[
    "SQL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTransformationType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowTransformationType:
    return cast(DataIntegrationFlowTransformationType, data)
