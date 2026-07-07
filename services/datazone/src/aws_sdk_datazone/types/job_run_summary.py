"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.job_run_error
    import aws_sdk_datazone.types.job_run_mode
    import aws_sdk_datazone.types.job_run_status
    import aws_sdk_datazone.types.job_type


class JobRunSummary(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The domain ID of the job run.</p>"""
    job_id: NotRequired["str"]
    """<p>The job ID of a job run.</p>"""
    job_type: NotRequired["aws_sdk_datazone.types.job_type.JobType"]
    """<p>The job type of a job run.</p>"""
    run_id: NotRequired["str"]
    """<p>The run ID of a job run.</p>"""
    run_mode: NotRequired["aws_sdk_datazone.types.job_run_mode.JobRunMode"]
    """<p>The run mode of a job run.</p>"""
    status: NotRequired["aws_sdk_datazone.types.job_run_status.JobRunStatus"]
    """<p>The status of a job run.</p>"""
    error: NotRequired["aws_sdk_datazone.types.job_run_error.JobRunError"]
    """<p>The error of a job run.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the job run.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which job run was created.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of a job run.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of a job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_type" in value:
        import aws_sdk_datazone.types.job_type

        out["jobType"] = aws_sdk_datazone.types.job_type.serialize_json(
            value["job_type"]
        )
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "run_mode" in value:
        import aws_sdk_datazone.types.job_run_mode

        out["runMode"] = aws_sdk_datazone.types.job_run_mode.serialize_json(
            value["run_mode"]
        )
    if "status" in value:
        import aws_sdk_datazone.types.job_run_status

        out["status"] = aws_sdk_datazone.types.job_run_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import aws_sdk_datazone.types.job_run_error

        out["error"] = aws_sdk_datazone.types.job_run_error.serialize_json(
            value["error"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "start_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["startTime"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["endTime"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> JobRunSummary:
    out: JobRunSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobType" in data:
        import aws_sdk_datazone.types.job_type

        out["job_type"] = aws_sdk_datazone.types.job_type.deserialize_json(
            data["jobType"]
        )
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "runMode" in data:
        import aws_sdk_datazone.types.job_run_mode

        out["run_mode"] = aws_sdk_datazone.types.job_run_mode.deserialize_json(
            data["runMode"]
        )
    if "status" in data:
        import aws_sdk_datazone.types.job_run_status

        out["status"] = aws_sdk_datazone.types.job_run_status.deserialize_json(
            data["status"]
        )
    if "error" in data:
        import aws_sdk_datazone.types.job_run_error

        out["error"] = aws_sdk_datazone.types.job_run_error.deserialize_json(
            data["error"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "startTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["start_time"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["end_time"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    return out
