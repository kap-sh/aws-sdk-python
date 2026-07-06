"""Generated from Smithy shape ``com.amazonaws.amplify#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.commit_id
    import aws_sdk_amplify.types.commit_message
    import aws_sdk_amplify.types.commit_time
    import aws_sdk_amplify.types.end_time
    import aws_sdk_amplify.types.job_arn
    import aws_sdk_amplify.types.job_id
    import aws_sdk_amplify.types.job_status
    import aws_sdk_amplify.types.job_type
    import aws_sdk_amplify.types.source_url
    import aws_sdk_amplify.types.source_url_type
    import aws_sdk_amplify.types.start_time


class JobSummary(TypedDict, closed=True):
    job_arn: "aws_sdk_amplify.types.job_arn.JobArn"
    """<p> The Amazon Resource Name (ARN) for the job. </p>"""
    job_id: "aws_sdk_amplify.types.job_id.JobId"
    """<p> The unique ID for the job. </p>"""
    commit_id: "aws_sdk_amplify.types.commit_id.CommitId"
    """<p> The commit ID from a third-party repository provider for the job. </p>"""
    commit_message: "aws_sdk_amplify.types.commit_message.CommitMessage"
    """<p> The commit message from a third-party repository provider for the job. </p>"""
    commit_time: "aws_sdk_amplify.types.commit_time.CommitTime"
    """<p>The commit date and time for the job. </p>"""
    start_time: "aws_sdk_amplify.types.start_time.StartTime"
    """<p> The start date and time for the job. </p>"""
    status: "aws_sdk_amplify.types.job_status.JobStatus"
    """<p> The current status for the job. </p>"""
    end_time: NotRequired["aws_sdk_amplify.types.end_time.EndTime"]
    """<p> The end date and time for the job. </p>"""
    job_type: "aws_sdk_amplify.types.job_type.JobType"
    """<p> The type for the job. If the value is <code>RELEASE</code>, the job was manually released from its source by using the <code>StartJob</code> API. This value is available only for apps that are connected to a repository.</p> <p>If the value is <code>RETRY</code>, the job was manually retried using the <code>StartJob</code> API. If the value is <code>WEB_HOOK</code>, the job was automatically triggered by webhooks. If the value is <code>MANUAL</code>, the job is for a manually deployed app. Manually deployed apps are not connected to a Git repository.</p>"""
    source_url: NotRequired["aws_sdk_amplify.types.source_url.SourceUrl"]
    """<p>The source URL for the files to deploy. The source URL can be either an HTTP GET URL that is publicly accessible and downloads a single .zip file, or an Amazon S3 bucket and prefix.</p>"""
    source_url_type: NotRequired["aws_sdk_amplify.types.source_url_type.SourceUrlType"]
    """<p>The type of source specified by the <code>sourceURL</code>. If the value is <code>ZIP</code>, the source is a .zip file. If the value is <code>BUCKET_PREFIX</code>, the source is an Amazon S3 bucket and prefix. If no value is specified, the default is <code>ZIP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobId"] = value["job_id"]
    out["commitId"] = value["commit_id"]
    out["commitMessage"] = value["commit_message"]
    import aws_sdk_amplify.types.commit_time

    out["commitTime"] = aws_sdk_amplify.types.commit_time.serialize_json(
        value["commit_time"]
    )
    import aws_sdk_amplify.types.start_time

    out["startTime"] = aws_sdk_amplify.types.start_time.serialize_json(
        value["start_time"]
    )
    import aws_sdk_amplify.types.job_status

    out["status"] = aws_sdk_amplify.types.job_status.serialize_json(value["status"])
    if "end_time" in value:
        import aws_sdk_amplify.types.end_time

        out["endTime"] = aws_sdk_amplify.types.end_time.serialize_json(
            value["end_time"]
        )
    import aws_sdk_amplify.types.job_type

    out["jobType"] = aws_sdk_amplify.types.job_type.serialize_json(value["job_type"])
    if "source_url" in value:
        out["sourceUrl"] = value["source_url"]
    if "source_url_type" in value:
        import aws_sdk_amplify.types.source_url_type

        out["sourceUrlType"] = aws_sdk_amplify.types.source_url_type.serialize_json(
            value["source_url_type"]
        )
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("JobSummary.job_arn required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobSummary.job_id required")
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("JobSummary.commit_id required")
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    else:
        raise DeserializationError("JobSummary.commit_message required")
    if "commitTime" in data:
        import aws_sdk_amplify.types.commit_time

        out["commit_time"] = aws_sdk_amplify.types.commit_time.deserialize_json(
            data["commitTime"]
        )
    else:
        raise DeserializationError("JobSummary.commit_time required")
    if "startTime" in data:
        import aws_sdk_amplify.types.start_time

        out["start_time"] = aws_sdk_amplify.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("JobSummary.start_time required")
    if "status" in data:
        import aws_sdk_amplify.types.job_status

        out["status"] = aws_sdk_amplify.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("JobSummary.status required")
    if "endTime" in data:
        import aws_sdk_amplify.types.end_time

        out["end_time"] = aws_sdk_amplify.types.end_time.deserialize_json(
            data["endTime"]
        )
    if "jobType" in data:
        import aws_sdk_amplify.types.job_type

        out["job_type"] = aws_sdk_amplify.types.job_type.deserialize_json(
            data["jobType"]
        )
    else:
        raise DeserializationError("JobSummary.job_type required")
    if "sourceUrl" in data:
        out["source_url"] = data["sourceUrl"]
    if "sourceUrlType" in data:
        import aws_sdk_amplify.types.source_url_type

        out["source_url_type"] = aws_sdk_amplify.types.source_url_type.deserialize_json(
            data["sourceUrlType"]
        )
    return out
