"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier

AdvancedPromptOptimizationJobIdentifiers: TypeAlias = list[
    "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationJobIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> AdvancedPromptOptimizationJobIdentifiers:
    return list(data)
