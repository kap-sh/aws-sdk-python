"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier


class BatchDeleteAdvancedPromptOptimizationJobError(TypedDict):
    job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The identifier of the job that could not be deleted.</p>"""
    code: "str"
    """<p>The error code for the deletion failure.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobError) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobError:
    out: BatchDeleteAdvancedPromptOptimizationJobError = {}  # type: ignore[typeddict-item]
    if "jobIdentifier" in data:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobError.job_identifier required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobError.code required"
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
