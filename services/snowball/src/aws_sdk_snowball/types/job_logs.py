"""Generated from Smithy shape ``com.amazonaws.snowball#JobLogs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class JobLogs(TypedDict):
    job_completion_report_uri: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>A link to an Amazon S3 presigned URL where the job completion report is located.</p>"""
    job_success_log_uri: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>A link to an Amazon S3 presigned URL where the job success log is located.</p>"""
    job_failure_log_uri: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>A link to an Amazon S3 presigned URL where the job failure log is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobLogs) -> dict:
    out: dict = {}
    if "job_completion_report_uri" in value:
        out["JobCompletionReportURI"] = value["job_completion_report_uri"]
    if "job_success_log_uri" in value:
        out["JobSuccessLogURI"] = value["job_success_log_uri"]
    if "job_failure_log_uri" in value:
        out["JobFailureLogURI"] = value["job_failure_log_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobLogs:
    out: JobLogs = {}  # type: ignore[typeddict-item]
    if "JobCompletionReportURI" in data:
        out["job_completion_report_uri"] = data["JobCompletionReportURI"]
    if "JobSuccessLogURI" in data:
        out["job_success_log_uri"] = data["JobSuccessLogURI"]
    if "JobFailureLogURI" in data:
        out["job_failure_log_uri"] = data["JobFailureLogURI"]
    return out
