"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDedupeStrategyType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowDedupeStrategyType: TypeAlias = Literal["FIELD_PRIORITY",]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDedupeStrategyType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowDedupeStrategyType:
    return cast(DataIntegrationFlowDedupeStrategyType, data)
