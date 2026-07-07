"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#GetDataAutomationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_data_automation_runtime.types.automation_job_status
    import aws_sdk_bedrock_data_automation_runtime.types.output_configuration


class GetDataAutomationStatusResponse(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.automation_job_status.AutomationJobStatus"
    ]
    """Job Status."""
    error_type: NotRequired["str"]
    """Error Type."""
    error_message: NotRequired["str"]
    """Error Message."""
    output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    ]
    """Output configuration."""
    job_submission_time: NotRequired["datetime.datetime"]
    """Job Submission time."""
    job_completion_time: NotRequired["datetime.datetime"]
    """Job completion time."""
    job_duration_in_seconds: NotRequired["int"]
    """Job duration in seconds."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataAutomationStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.automation_job_status

        out["status"] = (
            aws_sdk_bedrock_data_automation_runtime.types.automation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "output_configuration" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    if "job_submission_time" in value:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp

        out["jobSubmissionTime"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp.serialize_aws_json_1_1(
                value["job_submission_time"]
            )
        )
    if "job_completion_time" in value:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp

        out["jobCompletionTime"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp.serialize_aws_json_1_1(
                value["job_completion_time"]
            )
        )
    if "job_duration_in_seconds" in value:
        out["jobDurationInSeconds"] = value["job_duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataAutomationStatusResponse:
    out: GetDataAutomationStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.automation_job_status

        out["status"] = (
            aws_sdk_bedrock_data_automation_runtime.types.automation_job_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "outputConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    if "jobSubmissionTime" in data:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp

        out["job_submission_time"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["jobSubmissionTime"]
            )
        )
    if "jobCompletionTime" in data:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp

        out["job_completion_time"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["jobCompletionTime"]
            )
        )
    if "jobDurationInSeconds" in data:
        out["job_duration_in_seconds"] = data["jobDurationInSeconds"]
    return out
