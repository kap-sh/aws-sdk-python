"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#GetDataAutomationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_data_automation_runtime.types.automation_job_status
    import capo_bedrock_data_automation_runtime.types.output_configuration


class GetDataAutomationStatusResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_bedrock_data_automation_runtime.types.automation_job_status.AutomationJobStatus"
    ]
    """Job Status."""
    error_type: NotRequired["str"]
    """Error Type."""
    error_message: NotRequired["str"]
    """Error Message."""
    output_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
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
        import capo_bedrock_data_automation_runtime.types.automation_job_status

        out["status"] = (
            capo_bedrock_data_automation_runtime.types.automation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "output_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    if "job_submission_time" in value:
        import capo_bedrock_data_automation_runtime._protocol.serialize

        out["jobSubmissionTime"] = (
            capo_bedrock_data_automation_runtime._protocol.serialize.fmt_date_time(
                value["job_submission_time"]
            )
        )
    if "job_completion_time" in value:
        import capo_bedrock_data_automation_runtime._protocol.serialize

        out["jobCompletionTime"] = (
            capo_bedrock_data_automation_runtime._protocol.serialize.fmt_date_time(
                value["job_completion_time"]
            )
        )
    if "job_duration_in_seconds" in value:
        out["jobDurationInSeconds"] = value["job_duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataAutomationStatusResponse:
    out: GetDataAutomationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_data_automation_runtime.types.automation_job_status

        out["status"] = (
            capo_bedrock_data_automation_runtime.types.automation_job_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("errorType") is not None:
        out["error_type"] = data["errorType"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    if data.get("jobSubmissionTime") is not None:
        import datetime

        out["job_submission_time"] = datetime.datetime.fromisoformat(
            data["jobSubmissionTime"].replace("Z", "+00:00")
        )
    if data.get("jobCompletionTime") is not None:
        import datetime

        out["job_completion_time"] = datetime.datetime.fromisoformat(
            data["jobCompletionTime"].replace("Z", "+00:00")
        )
    if data.get("jobDurationInSeconds") is not None:
        out["job_duration_in_seconds"] = data["jobDurationInSeconds"]
    return out
