"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

BatchDeleteAdvancedPromptOptimizationJobErrors: TypeAlias = list[
    "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.BatchDeleteAdvancedPromptOptimizationJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobErrors) -> list:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteAdvancedPromptOptimizationJobErrors:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

    out: BatchDeleteAdvancedPromptOptimizationJobErrors = []
    for item in data:
        out.append(
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.deserialize_json(
                item
            )
        )
    return out
