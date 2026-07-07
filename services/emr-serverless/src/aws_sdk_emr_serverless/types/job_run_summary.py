"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.attempt_number
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.iam_role_arn
    import aws_sdk_emr_serverless.types.job_arn
    import aws_sdk_emr_serverless.types.job_run_id
    import aws_sdk_emr_serverless.types.job_run_mode
    import aws_sdk_emr_serverless.types.job_run_state
    import aws_sdk_emr_serverless.types.job_run_type
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.request_identity_user_arn
    import aws_sdk_emr_serverless.types.string256


class JobRunSummary(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application the job is running on.</p>"""
    id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The optional job run name. This doesn't have to be unique.</p>"""
    mode: NotRequired["aws_sdk_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run.</p>"""
    arn: "aws_sdk_emr_serverless.types.job_arn.JobArn"
    """<p>The ARN of the job run.</p>"""
    created_by: (
        "aws_sdk_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The user who created the job run.</p>"""
    created_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the job run was created.</p>"""
    updated_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the job run was last updated.</p>"""
    execution_role: "aws_sdk_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The execution role ARN of the job run.</p>"""
    state: "aws_sdk_emr_serverless.types.job_run_state.JobRunState"
    """<p>The state of the job run.</p>"""
    state_details: "aws_sdk_emr_serverless.types.string256.String256"
    """<p>The state details of the job run.</p>"""
    release_label: "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release associated with the application your job is running on.</p>"""
    type: NotRequired["aws_sdk_emr_serverless.types.job_run_type.JobRunType"]
    """<p>The type of job run, such as Spark or Hive.</p>"""
    attempt: NotRequired["aws_sdk_emr_serverless.types.attempt_number.AttemptNumber"]
    """<p>The attempt number of the job run execution.</p>"""
    attempt_created_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time of when the job run attempt was created.</p>"""
    attempt_updated_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time of when the job run attempt was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunSummary) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "mode" in value:
        out["mode"] = value["mode"]
    out["arn"] = value["arn"]
    out["createdBy"] = value["created_by"]
    import aws_sdk_emr_serverless.types.date

    out["createdAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import aws_sdk_emr_serverless.types.date

    out["updatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    out["executionRole"] = value["execution_role"]
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    if "type" in value:
        out["type"] = value["type"]
    if "attempt" in value:
        out["attempt"] = value["attempt"]
    if "attempt_created_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["attemptCreatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["attempt_created_at"]
        )
    if "attempt_updated_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["attemptUpdatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["attempt_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> JobRunSummary:
    out: JobRunSummary = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("JobRunSummary.application_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("JobRunSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "mode" in data:
        out["mode"] = data["mode"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("JobRunSummary.arn required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("JobRunSummary.created_by required")
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("JobRunSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("JobRunSummary.updated_at required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("JobRunSummary.execution_role required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("JobRunSummary.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    else:
        raise DeserializationError("JobRunSummary.state_details required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("JobRunSummary.release_label required")
    if "type" in data:
        out["type"] = data["type"]
    if "attempt" in data:
        out["attempt"] = data["attempt"]
    if "attemptCreatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["attempt_created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["attemptCreatedAt"]
        )
    if "attemptUpdatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["attempt_updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["attemptUpdatedAt"]
        )
    return out
