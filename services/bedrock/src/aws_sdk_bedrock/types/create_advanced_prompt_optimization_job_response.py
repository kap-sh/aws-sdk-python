"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAdvancedPromptOptimizationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn


class CreateAdvancedPromptOptimizationJobResponse(TypedDict):
    job_arn: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn.AdvancedPromptOptimizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the created advanced prompt optimization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAdvancedPromptOptimizationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateAdvancedPromptOptimizationJobResponse:
    out: CreateAdvancedPromptOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError(
            "CreateAdvancedPromptOptimizationJobResponse.job_arn required"
        )
    return out
