"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_entityresolution.types.job_id
    import aws_sdk_entityresolution.types.job_status


class JobSummary(TypedDict, closed=True):
    job_id: "aws_sdk_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    status: "aws_sdk_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import aws_sdk_entityresolution.types.job_status

    out["status"] = aws_sdk_entityresolution.types.job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["startTime"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobSummary.job_id required")
    if "status" in data:
        import aws_sdk_entityresolution.types.job_status

        out["status"] = aws_sdk_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("JobSummary.status required")
    if "startTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("JobSummary.start_time required")
    if "endTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    return out
