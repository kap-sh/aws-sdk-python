"""Generated from Smithy shape ``com.amazonaws.m2#GetBatchJobExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.batch_job_execution_status
    import aws_sdk_m2.types.batch_job_identifier
    import aws_sdk_m2.types.batch_job_type
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.job_step_restart_marker
    import aws_sdk_m2.types.string100
    import aws_sdk_m2.types.timestamp


class GetBatchJobExecutionResponse(TypedDict):
    execution_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier for this batch job execution.</p>"""
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""
    job_id: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The unique identifier for this batch job.</p>"""
    job_name: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The name of this batch job.</p>"""
    job_user: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The user for the job.</p>"""
    job_type: NotRequired["aws_sdk_m2.types.batch_job_type.BatchJobType"]
    """<p>The type of job.</p>"""
    status: "aws_sdk_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
    """<p>The status of the batch job execution.</p>"""
    start_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the batch job execution started.</p>"""
    end_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when the batch job execution ended.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    return_code: NotRequired["str"]
    """<p>The batch job return code from either the Blu Age or Micro Focus runtime engines. For more information, see <a href=\"https://www.ibm.com/docs/en/was/8.5.5?topic=model-batch-return-codes\">Batch return codes</a> in the <i>IBM WebSphere Application Server</i> documentation.</p>"""
    batch_job_identifier: NotRequired[
        "aws_sdk_m2.types.batch_job_identifier.BatchJobIdentifier"
    ]
    """<p>The unique identifier of this batch job.</p>"""
    job_step_restart_marker: NotRequired[
        "aws_sdk_m2.types.job_step_restart_marker.JobStepRestartMarker"
    ]
    """<p>The step/procedure step information for the restart batch job operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBatchJobExecutionResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["applicationId"] = value["application_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_user" in value:
        out["jobUser"] = value["job_user"]
    if "job_type" in value:
        out["jobType"] = value["job_type"]
    out["status"] = value["status"]
    import aws_sdk_m2.types.timestamp

    out["startTime"] = aws_sdk_m2.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import aws_sdk_m2.types.timestamp

        out["endTime"] = aws_sdk_m2.types.timestamp.serialize_json(value["end_time"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "return_code" in value:
        out["returnCode"] = value["return_code"]
    if "batch_job_identifier" in value:
        import aws_sdk_m2.types.batch_job_identifier

        out["batchJobIdentifier"] = (
            aws_sdk_m2.types.batch_job_identifier.serialize_json(
                value["batch_job_identifier"]
            )
        )
    if "job_step_restart_marker" in value:
        import aws_sdk_m2.types.job_step_restart_marker

        out["jobStepRestartMarker"] = (
            aws_sdk_m2.types.job_step_restart_marker.serialize_json(
                value["job_step_restart_marker"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBatchJobExecutionResponse:
    out: GetBatchJobExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("GetBatchJobExecutionResponse.execution_id required")
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError(
            "GetBatchJobExecutionResponse.application_id required"
        )
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobUser" in data:
        out["job_user"] = data["jobUser"]
    if "jobType" in data:
        out["job_type"] = data["jobType"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetBatchJobExecutionResponse.status required")
    if "startTime" in data:
        import aws_sdk_m2.types.timestamp

        out["start_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetBatchJobExecutionResponse.start_time required")
    if "endTime" in data:
        import aws_sdk_m2.types.timestamp

        out["end_time"] = aws_sdk_m2.types.timestamp.deserialize_json(data["endTime"])
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "returnCode" in data:
        out["return_code"] = data["returnCode"]
    if "batchJobIdentifier" in data:
        import aws_sdk_m2.types.batch_job_identifier

        out["batch_job_identifier"] = (
            aws_sdk_m2.types.batch_job_identifier.deserialize_json(
                data["batchJobIdentifier"]
            )
        )
    if "jobStepRestartMarker" in data:
        import aws_sdk_m2.types.job_step_restart_marker

        out["job_step_restart_marker"] = (
            aws_sdk_m2.types.job_step_restart_marker.deserialize_json(
                data["jobStepRestartMarker"]
            )
        )
    return out
