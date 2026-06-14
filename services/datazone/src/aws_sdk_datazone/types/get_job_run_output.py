"""Generated from Smithy shape ``com.amazonaws.datazone#GetJobRunOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.job_run_details
    import aws_sdk_datazone.types.job_run_error
    import aws_sdk_datazone.types.job_run_mode
    import aws_sdk_datazone.types.job_run_status
    import aws_sdk_datazone.types.job_type


class GetJobRunOutput(TypedDict):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the job run.</p>"""
    job_id: NotRequired["str"]
    """<p>The ID of the job run.</p>"""
    job_type: NotRequired["aws_sdk_datazone.types.job_type.JobType"]
    """<p>The type of the job run.</p>"""
    run_mode: NotRequired["aws_sdk_datazone.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run.</p>"""
    details: NotRequired["aws_sdk_datazone.types.job_run_details.JobRunDetails"]
    """<p>The details of the job run.</p>"""
    status: NotRequired["aws_sdk_datazone.types.job_run_status.JobRunStatus"]
    """<p>The status of the job run.</p>"""
    error: NotRequired["aws_sdk_datazone.types.job_run_error.JobRunError"]
    """<p>The error generated if the action is not completed successfully.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the job run.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run was created.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the job run ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_type" in value:
        import aws_sdk_datazone.types.job_type

        out["jobType"] = aws_sdk_datazone.types.job_type.serialize_json(
            value["job_type"]
        )
    if "run_mode" in value:
        import aws_sdk_datazone.types.job_run_mode

        out["runMode"] = aws_sdk_datazone.types.job_run_mode.serialize_json(
            value["run_mode"]
        )
    if "details" in value:
        import aws_sdk_datazone.types.job_run_details

        out["details"] = aws_sdk_datazone.types.job_run_details.serialize_json(
            value["details"]
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


def deserialize_json(data: dict) -> GetJobRunOutput:
    out: GetJobRunOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobType" in data:
        import aws_sdk_datazone.types.job_type

        out["job_type"] = aws_sdk_datazone.types.job_type.deserialize_json(
            data["jobType"]
        )
    if "runMode" in data:
        import aws_sdk_datazone.types.job_run_mode

        out["run_mode"] = aws_sdk_datazone.types.job_run_mode.deserialize_json(
            data["runMode"]
        )
    if "details" in data:
        import aws_sdk_datazone.types.job_run_details

        out["details"] = aws_sdk_datazone.types.job_run_details.deserialize_json(
            data["details"]
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
