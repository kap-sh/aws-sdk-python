"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobSummariesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_job_summary_list
    import aws_sdk_backup.types.string


class ListScanJobSummariesOutput(TypedDict, closed=True):
    scan_job_summaries: NotRequired[
        "aws_sdk_backup.types.scan_job_summary_list.ScanJobSummaryList"
    ]
    """<p>The summary information.</p>"""
    aggregation_period: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code>The daily job count for the prior 1 day.</p> </li> <li> <p> <code>SEVEN_DAYS</code>The daily job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code>The daily job count for the prior 14 days.</p> </li> </ul> <p>Valid Values: <code>'ONE_DAY'</code> | <code>'SEVEN_DAYS'</code> | <code>'FOURTEEN_DAYS'</code> </p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScanJobSummariesOutput) -> dict:
    out: dict = {}
    if "scan_job_summaries" in value:
        import aws_sdk_backup.types.scan_job_summary_list

        out["ScanJobSummaries"] = (
            aws_sdk_backup.types.scan_job_summary_list.serialize_json(
                value["scan_job_summaries"]
            )
        )
    if "aggregation_period" in value:
        out["AggregationPeriod"] = value["aggregation_period"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScanJobSummariesOutput:
    out: ListScanJobSummariesOutput = {}  # type: ignore[typeddict-item]
    if "ScanJobSummaries" in data:
        import aws_sdk_backup.types.scan_job_summary_list

        out["scan_job_summaries"] = (
            aws_sdk_backup.types.scan_job_summary_list.deserialize_json(
                data["ScanJobSummaries"]
            )
        )
    if "AggregationPeriod" in data:
        out["aggregation_period"] = data["AggregationPeriod"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
