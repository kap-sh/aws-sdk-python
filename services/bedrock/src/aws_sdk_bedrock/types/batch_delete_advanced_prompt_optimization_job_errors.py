"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

BatchDeleteAdvancedPromptOptimizationJobErrors: TypeAlias = list[
    "aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.BatchDeleteAdvancedPromptOptimizationJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobErrors) -> list:
    import aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteAdvancedPromptOptimizationJobErrors:
    import aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error

    out: BatchDeleteAdvancedPromptOptimizationJobErrors = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_error.deserialize_json(
                item
            )
        )
    return out
