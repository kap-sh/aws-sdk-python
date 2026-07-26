"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.job_id
    import capo_entityresolution.types.job_status


class JobSummary(TypedDict, closed=True):
    job_id: "capo_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    status: "capo_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_entityresolution.types.job_status

    out["status"] = capo_entityresolution.types.job_status.serialize_json(
        value["status"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["startTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_entityresolution.types._prelude.timestamp

        out["endTime"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobSummary.job_id required")
    if "status" in data:
        import capo_entityresolution.types.job_status

        out["status"] = capo_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("JobSummary.status required")
    if "startTime" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("JobSummary.start_time required")
    if "endTime" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    return out
