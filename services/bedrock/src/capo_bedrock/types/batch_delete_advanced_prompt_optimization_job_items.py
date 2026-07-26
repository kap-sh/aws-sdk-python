"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item

BatchDeleteAdvancedPromptOptimizationJobItems: TypeAlias = list[
    "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item.BatchDeleteAdvancedPromptOptimizationJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobItems) -> list:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteAdvancedPromptOptimizationJobItems:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item

    out: BatchDeleteAdvancedPromptOptimizationJobItems = []
    for item in data:
        out.append(
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_item.deserialize_json(
                item
            )
        )
    return out
