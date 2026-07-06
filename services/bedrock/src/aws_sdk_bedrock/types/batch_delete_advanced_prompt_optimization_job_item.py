"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status


class BatchDeleteAdvancedPromptOptimizationJobItem(TypedDict, closed=True):
    job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The identifier of the deleted job.</p>"""
    job_status: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the deleted job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobItem) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobItem:
    out: BatchDeleteAdvancedPromptOptimizationJobItem = {}  # type: ignore[typeddict-item]
    if "jobIdentifier" in data:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobItem.job_identifier required"
        )
    if "jobStatus" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status

        out["job_status"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteAdvancedPromptOptimizationJobItem.job_status required"
        )
    return out
