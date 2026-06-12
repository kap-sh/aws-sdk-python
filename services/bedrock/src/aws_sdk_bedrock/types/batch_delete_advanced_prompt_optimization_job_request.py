"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers


class BatchDeleteAdvancedPromptOptimizationJobRequest(TypedDict):
    job_identifiers: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers"
    """<p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers

    out["jobIdentifiers"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers.serialize_json(
            value["job_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobRequest:
    out: BatchDeleteAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if "jobIdentifiers" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers

        out["job_identifiers"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers.deserialize_json(
                data["jobIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobRequest.job_identifiers required"
        )
    return out
