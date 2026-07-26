"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.exit_message
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.processing_job_arn
    import capo_sagemaker.types.processing_job_name
    import capo_sagemaker.types.processing_job_status
    import capo_sagemaker.types.timestamp


class ProcessingJobSummary(TypedDict, closed=True):
    processing_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the processing job.</p>"""
    processing_job_arn: NotRequired[
        "capo_sagemaker.types.processing_job_arn.ProcessingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the processing job..</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job was created.</p>"""
    processing_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job completed.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates the last time the processing job was modified.</p>"""
    processing_job_status: NotRequired[
        "capo_sagemaker.types.processing_job_status.ProcessingJobStatus"
    ]
    """<p>The status of the processing job.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>A string, up to one KB in size, that contains the reason a processing job failed, if it failed.</p>"""
    exit_message: NotRequired["capo_sagemaker.types.exit_message.ExitMessage"]
    """<p>An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingJobSummary) -> dict:
    out: dict = {}
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    if "processing_job_arn" in value:
        out["ProcessingJobArn"] = value["processing_job_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "processing_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["ProcessingEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["processing_end_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "processing_job_status" in value:
        import capo_sagemaker.types.processing_job_status

        out["ProcessingJobStatus"] = (
            capo_sagemaker.types.processing_job_status.serialize_aws_json_1_1(
                value["processing_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "exit_message" in value:
        out["ExitMessage"] = value["exit_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingJobSummary:
    out: ProcessingJobSummary = {}  # type: ignore[typeddict-item]
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    if "ProcessingJobArn" in data:
        out["processing_job_arn"] = data["ProcessingJobArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "ProcessingEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["processing_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ProcessingEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "ProcessingJobStatus" in data:
        import capo_sagemaker.types.processing_job_status

        out["processing_job_status"] = (
            capo_sagemaker.types.processing_job_status.deserialize_aws_json_1_1(
                data["ProcessingJobStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ExitMessage" in data:
        out["exit_message"] = data["ExitMessage"]
    return out
