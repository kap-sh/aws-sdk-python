"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowRuleDefinitionType``."""

from typing import Literal, TypeAlias, cast

IdMappingWorkflowRuleDefinitionType: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowRuleDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingWorkflowRuleDefinitionType:
    return cast(IdMappingWorkflowRuleDefinitionType, data)
