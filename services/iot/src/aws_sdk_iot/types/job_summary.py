"""Generated from Smithy shape ``com.amazonaws.iot#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean_wrapper_object
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.job_arn
    import aws_sdk_iot.types.job_id
    import aws_sdk_iot.types.job_status
    import aws_sdk_iot.types.target_selection
    import aws_sdk_iot.types.thing_group_id


class JobSummary(TypedDict, closed=True):
    job_arn: NotRequired["aws_sdk_iot.types.job_arn.JobArn"]
    """<p>The job ARN.</p>"""
    job_id: NotRequired["aws_sdk_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    thing_group_id: NotRequired["aws_sdk_iot.types.thing_group_id.ThingGroupId"]
    """<p>The ID of the thing group.</p>"""
    target_selection: NotRequired["aws_sdk_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.</p> <note> <p>We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.</p> </note>"""
    status: NotRequired["aws_sdk_iot.types.job_status.JobStatus"]
    """<p>The job summary status.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job was last updated.</p>"""
    completed_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job completed.</p>"""
    is_concurrent: NotRequired[
        "aws_sdk_iot.types.boolean_wrapper_object.BooleanWrapperObject"
    ]
    """<p>Indicates whether a job is concurrent. Will be true when a job is rolling out new job executions or canceling previously created executions, otherwise false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "thing_group_id" in value:
        out["thingGroupId"] = value["thing_group_id"]
    if "target_selection" in value:
        import aws_sdk_iot.types.target_selection

        out["targetSelection"] = aws_sdk_iot.types.target_selection.serialize_json(
            value["target_selection"]
        )
    if "status" in value:
        import aws_sdk_iot.types.job_status

        out["status"] = aws_sdk_iot.types.job_status.serialize_json(value["status"])
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "completed_at" in value:
        import aws_sdk_iot.types.date_type

        out["completedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["completed_at"]
        )
    if "is_concurrent" in value:
        out["isConcurrent"] = value["is_concurrent"]
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "thingGroupId" in data:
        out["thing_group_id"] = data["thingGroupId"]
    if "targetSelection" in data:
        import aws_sdk_iot.types.target_selection

        out["target_selection"] = aws_sdk_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
        )
    if "status" in data:
        import aws_sdk_iot.types.job_status

        out["status"] = aws_sdk_iot.types.job_status.deserialize_json(data["status"])
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "completedAt" in data:
        import aws_sdk_iot.types.date_type

        out["completed_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["completedAt"]
        )
    if "isConcurrent" in data:
        out["is_concurrent"] = data["isConcurrent"]
    return out
