"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_job_error_code
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.string


class BatchUpdateJobError(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the job that could not be updated.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the job that could not be updated.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the job that could not be updated.</p>"""
    code: "aws_sdk_deadline.types.batch_update_job_error_code.BatchUpdateJobErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_deadline.types.string.String"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    import aws_sdk_deadline.types.batch_update_job_error_code

    out["code"] = aws_sdk_deadline.types.batch_update_job_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateJobError:
    out: BatchUpdateJobError = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchUpdateJobError.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchUpdateJobError.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchUpdateJobError.job_id required")
    if "code" in data:
        import aws_sdk_deadline.types.batch_update_job_error_code

        out["code"] = (
            aws_sdk_deadline.types.batch_update_job_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateJobError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchUpdateJobError.message required")
    return out
