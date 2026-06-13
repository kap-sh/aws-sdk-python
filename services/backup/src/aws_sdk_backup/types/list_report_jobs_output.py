"""Generated from Smithy shape ``com.amazonaws.backup#ListReportJobsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_job_list
    import aws_sdk_backup.types.string


class ListReportJobsOutput(TypedDict):
    report_jobs: NotRequired["aws_sdk_backup.types.report_job_list.ReportJobList"]
    """<p>Details about your report jobs in JSON format.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportJobsOutput) -> dict:
    out: dict = {}
    if "report_jobs" in value:
        import aws_sdk_backup.types.report_job_list

        out["ReportJobs"] = aws_sdk_backup.types.report_job_list.serialize_json(
            value["report_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportJobsOutput:
    out: ListReportJobsOutput = {}  # type: ignore[typeddict-item]
    if "ReportJobs" in data:
        import aws_sdk_backup.types.report_job_list

        out["report_jobs"] = aws_sdk_backup.types.report_job_list.deserialize_json(
            data["ReportJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
