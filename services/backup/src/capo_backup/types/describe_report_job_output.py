"""Generated from Smithy shape ``com.amazonaws.backup#DescribeReportJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.report_job


class DescribeReportJobOutput(TypedDict, closed=True):
    report_job: NotRequired["capo_backup.types.report_job.ReportJob"]
    """<p>The information about a report job, including its completion and creation times, report destination, unique report job ID, Amazon Resource Name (ARN), report template, status, and status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReportJobOutput) -> dict:
    out: dict = {}
    if "report_job" in value:
        import capo_backup.types.report_job

        out["ReportJob"] = capo_backup.types.report_job.serialize_json(
            value["report_job"]
        )
    return out


def deserialize_json(data: dict) -> DescribeReportJobOutput:
    out: DescribeReportJobOutput = {}  # type: ignore[typeddict-item]
    if "ReportJob" in data:
        import capo_backup.types.report_job

        out["report_job"] = capo_backup.types.report_job.deserialize_json(
            data["ReportJob"]
        )
    return out
