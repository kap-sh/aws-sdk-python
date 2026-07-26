"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items


class BatchDeleteAdvancedPromptOptimizationJobResponse(TypedDict, closed=True):
    errors: "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors.BatchDeleteAdvancedPromptOptimizationJobErrors"
    """<p>A list of errors encountered during batch deletion.</p>"""
    advanced_prompt_optimization_jobs: "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items.BatchDeleteAdvancedPromptOptimizationJobItems"
    """<p>A list of successfully deleted advanced prompt optimization jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors

    out["errors"] = (
        capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors.serialize_json(
            value["errors"]
        )
    )
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items

    out["advancedPromptOptimizationJobs"] = (
        capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items.serialize_json(
            value["advanced_prompt_optimization_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobResponse:
    out: BatchDeleteAdvancedPromptOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors

        out["errors"] = (
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobResponse.errors required"
        )
    if "advancedPromptOptimizationJobs" in data:
        import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items

        out["advanced_prompt_optimization_jobs"] = (
            capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_items.deserialize_json(
                data["advancedPromptOptimizationJobs"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobResponse.advanced_prompt_optimization_jobs required"
        )
    return out
