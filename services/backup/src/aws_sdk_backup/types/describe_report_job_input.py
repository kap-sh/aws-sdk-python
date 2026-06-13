"""Generated from Smithy shape ``com.amazonaws.backup#DescribeReportJobInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_job_id


class DescribeReportJobInput(TypedDict):
    report_job_id: "aws_sdk_backup.types.report_job_id.ReportJobId"
    """<p>The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReportJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReportJobInput:
    out: DescribeReportJobInput = {}  # type: ignore[typeddict-item]
    return out
