"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeSortOrder``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowFieldPriorityDedupeSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowFieldPriorityDedupeSortOrder) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowFieldPriorityDedupeSortOrder:
    return cast(DataIntegrationFlowFieldPriorityDedupeSortOrder, data)
