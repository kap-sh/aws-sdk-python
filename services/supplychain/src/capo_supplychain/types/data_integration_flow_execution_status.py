"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowExecutionStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowExecutionStatus:
    return cast(DataIntegrationFlowExecutionStatus, data)
