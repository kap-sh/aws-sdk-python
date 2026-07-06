"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#JobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.job_error
    import aws_sdk_accessanalyzer.types.job_id
    import aws_sdk_accessanalyzer.types.job_status
    import aws_sdk_accessanalyzer.types.timestamp


class JobDetails(TypedDict, closed=True):
    job_id: "aws_sdk_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""
    status: "aws_sdk_accessanalyzer.types.job_status.JobStatus"
    """<p>The status of the job request.</p>"""
    started_on: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>A timestamp of when the job was started.</p>"""
    completed_on: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>A timestamp of when the job was completed.</p>"""
    job_error: NotRequired["aws_sdk_accessanalyzer.types.job_error.JobError"]
    """<p>The job error for the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetails) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["status"] = value["status"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["startedOn"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["started_on"]
    )
    if "completed_on" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completedOn"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["completed_on"]
        )
    if "job_error" in value:
        import aws_sdk_accessanalyzer.types.job_error

        out["jobError"] = aws_sdk_accessanalyzer.types.job_error.serialize_json(
            value["job_error"]
        )
    return out


def deserialize_json(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobDetails.job_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("JobDetails.status required")
    if "startedOn" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["started_on"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["startedOn"]
        )
    else:
        raise DeserializationError("JobDetails.started_on required")
    if "completedOn" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completed_on"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["completedOn"]
        )
    if "jobError" in data:
        import aws_sdk_accessanalyzer.types.job_error

        out["job_error"] = aws_sdk_accessanalyzer.types.job_error.deserialize_json(
            data["jobError"]
        )
    return out
