"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.batch_inference_job_mode
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class BatchInferenceJobSummary(TypedDict, closed=True):
    batch_inference_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the batch inference job.</p>"""
    job_name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the batch inference job.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the batch inference job. The status is one of the following values:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>IN PROGRESS</p> </li> <li> <p>ACTIVE</p> </li> <li> <p>CREATE FAILED</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The time at which the batch inference job was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The time at which the batch inference job was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If the batch inference job failed, the reason for the failure.</p>"""
    solution_version_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the solution version used by the batch inference job.</p>"""
    batch_inference_job_mode: NotRequired[
        "aws_sdk_personalize.types.batch_inference_job_mode.BatchInferenceJobMode"
    ]
    """<p>The job's mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobSummary) -> dict:
    out: dict = {}
    if "batch_inference_job_arn" in value:
        out["batchInferenceJobArn"] = value["batch_inference_job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "batch_inference_job_mode" in value:
        import aws_sdk_personalize.types.batch_inference_job_mode

        out["batchInferenceJobMode"] = (
            aws_sdk_personalize.types.batch_inference_job_mode.serialize_aws_json_1_1(
                value["batch_inference_job_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchInferenceJobSummary:
    out: BatchInferenceJobSummary = {}  # type: ignore[typeddict-item]
    if "batchInferenceJobArn" in data:
        out["batch_inference_job_arn"] = data["batchInferenceJobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if "batchInferenceJobMode" in data:
        import aws_sdk_personalize.types.batch_inference_job_mode

        out["batch_inference_job_mode"] = (
            aws_sdk_personalize.types.batch_inference_job_mode.deserialize_aws_json_1_1(
                data["batchInferenceJobMode"]
            )
        )
    return out
