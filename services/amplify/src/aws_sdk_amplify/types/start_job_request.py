"""Generated from Smithy shape ``com.amazonaws.amplify#StartJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.commit_id
    import aws_sdk_amplify.types.commit_message
    import aws_sdk_amplify.types.commit_time
    import aws_sdk_amplify.types.job_id
    import aws_sdk_amplify.types.job_reason
    import aws_sdk_amplify.types.job_type


class StartJobRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p>The name of the branch to use for the job. </p>"""
    job_id: NotRequired["aws_sdk_amplify.types.job_id.JobId"]
    """<p>The unique ID for an existing job. This is required if the value of <code>jobType</code> is <code>RETRY</code>. </p>"""
    job_type: "aws_sdk_amplify.types.job_type.JobType"
    """<p>Describes the type for the job. The job type <code>RELEASE</code> starts a new job with the latest change from the specified branch. This value is available only for apps that are connected to a repository. </p> <p>The job type <code>RETRY</code> retries an existing job. If the job type value is <code>RETRY</code>, the <code>jobId</code> is also required. </p>"""
    job_reason: NotRequired["aws_sdk_amplify.types.job_reason.JobReason"]
    """<p>A descriptive reason for starting the job.</p>"""
    commit_id: NotRequired["aws_sdk_amplify.types.commit_id.CommitId"]
    """<p> The commit ID from a third-party repository provider for the job. </p>"""
    commit_message: NotRequired["aws_sdk_amplify.types.commit_message.CommitMessage"]
    """<p> The commit message from a third-party repository provider for the job. </p>"""
    commit_time: NotRequired["aws_sdk_amplify.types.commit_time.CommitTime"]
    """<p> The commit date and time for the job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    import aws_sdk_amplify.types.job_type

    out["jobType"] = aws_sdk_amplify.types.job_type.serialize_json(value["job_type"])
    if "job_reason" in value:
        out["jobReason"] = value["job_reason"]
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "commit_time" in value:
        import aws_sdk_amplify.types.commit_time

        out["commitTime"] = aws_sdk_amplify.types.commit_time.serialize_json(
            value["commit_time"]
        )
    return out


def deserialize_json(data: dict) -> StartJobRequest:
    out: StartJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobType" in data:
        import aws_sdk_amplify.types.job_type

        out["job_type"] = aws_sdk_amplify.types.job_type.deserialize_json(
            data["jobType"]
        )
    else:
        raise DeserializationError("StartJobRequest.job_type required")
    if "jobReason" in data:
        out["job_reason"] = data["jobReason"]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    if "commitTime" in data:
        import aws_sdk_amplify.types.commit_time

        out["commit_time"] = aws_sdk_amplify.types.commit_time.deserialize_json(
            data["commitTime"]
        )
    return out
