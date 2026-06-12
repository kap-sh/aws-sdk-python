"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_name
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status
    import aws_sdk_bedrock.types.timestamp


class AdvancedPromptOptimizationJobSummary(TypedDict):
    job_arn: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn.AdvancedPromptOptimizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_name: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName"
    """<p>The name of the job.</p>"""
    job_status: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the job.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the job was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the job was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastModifiedTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> AdvancedPromptOptimizationJobSummary:
    out: AdvancedPromptOptimizationJobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError(
            "AdvancedPromptOptimizationJobSummary.job_arn required"
        )
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError(
            "AdvancedPromptOptimizationJobSummary.job_name required"
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
            "AdvancedPromptOptimizationJobSummary.job_status required"
        )
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "AdvancedPromptOptimizationJobSummary.creation_time required"
        )
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_modified_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    return out
