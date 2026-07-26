"""Generated from Smithy shape ``com.amazonaws.bedrock#StopAdvancedPromptOptimizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier


class StopAdvancedPromptOptimizationJobRequest(TypedDict, closed=True):
    job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The ARN or ID of the advanced prompt optimization job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopAdvancedPromptOptimizationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopAdvancedPromptOptimizationJobRequest:
    out: StopAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    return out
