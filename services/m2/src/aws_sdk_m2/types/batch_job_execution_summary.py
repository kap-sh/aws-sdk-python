"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobExecutionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.batch_job_execution_status
    import aws_sdk_m2.types.batch_job_identifier
    import aws_sdk_m2.types.batch_job_type
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.string100
    import aws_sdk_m2.types.timestamp


class BatchJobExecutionSummary(TypedDict):
    execution_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of this execution of the batch job.</p>"""
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application that hosts this batch job.</p>"""
    job_id: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The unique identifier of a particular batch job.</p>"""
    job_name: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The name of a particular batch job.</p>"""
    job_type: NotRequired["aws_sdk_m2.types.batch_job_type.BatchJobType"]
    """<p>The type of a particular batch job execution.</p>"""
    status: "aws_sdk_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
    """<p>The status of a particular batch job execution.</p>"""
    start_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when a particular batch job execution started.</p>"""
    end_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when this batch job execution ended.</p>"""
    return_code: NotRequired["str"]
    r"""<p>The batch job return code from either the Blu Age or Micro Focus runtime engines. For more information, see <a href=\"https://www.ibm.com/docs/en/was/8.5.5?topic=model-batch-return-codes\">Batch return codes</a> in the <i>IBM WebSphere Application Server</i> documentation.</p>"""
    batch_job_identifier: NotRequired[
        "aws_sdk_m2.types.batch_job_identifier.BatchJobIdentifier"
    ]
    """<p>The unique identifier of this batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobExecutionSummary) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["applicationId"] = value["application_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_type" in value:
        out["jobType"] = value["job_type"]
    out["status"] = value["status"]
    import aws_sdk_m2.types.timestamp

    out["startTime"] = aws_sdk_m2.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import aws_sdk_m2.types.timestamp

        out["endTime"] = aws_sdk_m2.types.timestamp.serialize_json(value["end_time"])
    if "return_code" in value:
        out["returnCode"] = value["return_code"]
    if "batch_job_identifier" in value:
        import aws_sdk_m2.types.batch_job_identifier

        out["batchJobIdentifier"] = (
            aws_sdk_m2.types.batch_job_identifier.serialize_json(
                value["batch_job_identifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchJobExecutionSummary:
    out: BatchJobExecutionSummary = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.execution_id required")
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.application_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobType" in data:
        out["job_type"] = data["jobType"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("BatchJobExecutionSummary.status required")
    if "startTime" in data:
        import aws_sdk_m2.types.timestamp

        out["start_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("BatchJobExecutionSummary.start_time required")
    if "endTime" in data:
        import aws_sdk_m2.types.timestamp

        out["end_time"] = aws_sdk_m2.types.timestamp.deserialize_json(data["endTime"])
    if "returnCode" in data:
        out["return_code"] = data["returnCode"]
    if "batchJobIdentifier" in data:
        import aws_sdk_m2.types.batch_job_identifier

        out["batch_job_identifier"] = (
            aws_sdk_m2.types.batch_job_identifier.deserialize_json(
                data["batchJobIdentifier"]
            )
        )
    return out
