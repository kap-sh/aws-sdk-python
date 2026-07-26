"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_summary

AdvancedPromptOptimizationJobSummaries: TypeAlias = list[
    "capo_bedrock.types.advanced_prompt_optimization_job_summary.AdvancedPromptOptimizationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationJobSummaries) -> list:
    import capo_bedrock.types.advanced_prompt_optimization_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.advanced_prompt_optimization_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AdvancedPromptOptimizationJobSummaries:
    import capo_bedrock.types.advanced_prompt_optimization_job_summary

    out: AdvancedPromptOptimizationJobSummaries = []
    for item in data:
        out.append(
            capo_bedrock.types.advanced_prompt_optimization_job_summary.deserialize_json(
                item
            )
        )
    return out
