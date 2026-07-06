"""Generated from Smithy shape ``com.amazonaws.backup#StartReportJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_job_id


class StartReportJobOutput(TypedDict, closed=True):
    report_job_id: NotRequired["aws_sdk_backup.types.report_job_id.ReportJobId"]
    """<p>The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReportJobOutput) -> dict:
    out: dict = {}
    if "report_job_id" in value:
        out["ReportJobId"] = value["report_job_id"]
    return out


def deserialize_json(data: dict) -> StartReportJobOutput:
    out: StartReportJobOutput = {}  # type: ignore[typeddict-item]
    if "ReportJobId" in data:
        out["report_job_id"] = data["ReportJobId"]
    return out
