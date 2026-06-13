"""Generated from Smithy shape ``com.amazonaws.backup#ListReportJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.report_plan_name
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class ListReportJobsInput(TypedDict):
    by_report_plan_name: NotRequired[
        "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    ]
    """<p>Returns only report jobs with the specified report plan name.</p>"""
    by_creation_before: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.</p>"""
    by_creation_after: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.</p>"""
    by_status: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Returns only report jobs that are in the specified status. The statuses are:</p> <p> <code>CREATED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_ISSUES</code> </p> <p> Please note that only scanning jobs finish with state completed with issues. For backup jobs this is a console interpretation of a job that finishes in completed state and has a status message.</p>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReportJobsInput:
    out: ListReportJobsInput = {}  # type: ignore[typeddict-item]
    return out
