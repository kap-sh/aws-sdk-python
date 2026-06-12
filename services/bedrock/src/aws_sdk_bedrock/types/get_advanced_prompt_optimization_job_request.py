"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAdvancedPromptOptimizationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier


class GetAdvancedPromptOptimizationJobRequest(TypedDict):
    job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The ARN or ID of the advanced prompt optimization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdvancedPromptOptimizationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAdvancedPromptOptimizationJobRequest:
    out: GetAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    return out
