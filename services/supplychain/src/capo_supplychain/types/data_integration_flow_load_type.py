"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowLoadType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowLoadType: TypeAlias = Literal[
    "INCREMENTAL",
    "REPLACE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowLoadType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowLoadType:
    return cast(DataIntegrationFlowLoadType, data)
