"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_entity_error_code
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.string


class JobDetailsError(TypedDict, closed=True):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    code: "aws_sdk_deadline.types.job_entity_error_code.JobEntityErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_deadline.types.string.String"
    """<p>The error message detailing the error's cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsError) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import aws_sdk_deadline.types.job_entity_error_code

    out["code"] = aws_sdk_deadline.types.job_entity_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> JobDetailsError:
    out: JobDetailsError = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobDetailsError.job_id required")
    if "code" in data:
        import aws_sdk_deadline.types.job_entity_error_code

        out["code"] = aws_sdk_deadline.types.job_entity_error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("JobDetailsError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("JobDetailsError.message required")
    return out
