"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_error_code
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.string


class BatchGetSessionError(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session that could not be retrieved.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session that could not be retrieved.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the session that could not be retrieved.</p>"""
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID of the session that could not be retrieved.</p>"""
    code: "aws_sdk_deadline.types.batch_get_session_error_code.BatchGetSessionErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_deadline.types.string.String"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_deadline.types.batch_get_session_error_code

    out["code"] = aws_sdk_deadline.types.batch_get_session_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSessionError:
    out: BatchGetSessionError = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetSessionError.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetSessionError.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetSessionError.job_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("BatchGetSessionError.session_id required")
    if "code" in data:
        import aws_sdk_deadline.types.batch_get_session_error_code

        out["code"] = (
            aws_sdk_deadline.types.batch_get_session_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetSessionError.message required")
    return out
