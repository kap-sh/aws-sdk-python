"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupJobSummariesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_job_summary_list
    import aws_sdk_backup.types.string


class ListBackupJobSummariesOutput(TypedDict):
    backup_job_summaries: NotRequired[
        "aws_sdk_backup.types.backup_job_summary_list.BackupJobSummaryList"
    ]
    """<p>The summary information.</p>"""
    aggregation_period: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code> - The daily job count for the prior 14 days.</p> </li> <li> <p> <code>SEVEN_DAYS</code> - The aggregated job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code> - The aggregated job count for prior 14 days.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupJobSummariesOutput) -> dict:
    out: dict = {}
    if "backup_job_summaries" in value:
        import aws_sdk_backup.types.backup_job_summary_list

        out["BackupJobSummaries"] = (
            aws_sdk_backup.types.backup_job_summary_list.serialize_json(
                value["backup_job_summaries"]
            )
        )
    if "aggregation_period" in value:
        out["AggregationPeriod"] = value["aggregation_period"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackupJobSummariesOutput:
    out: ListBackupJobSummariesOutput = {}  # type: ignore[typeddict-item]
    if "BackupJobSummaries" in data:
        import aws_sdk_backup.types.backup_job_summary_list

        out["backup_job_summaries"] = (
            aws_sdk_backup.types.backup_job_summary_list.deserialize_json(
                data["BackupJobSummaries"]
            )
        )
    if "AggregationPeriod" in data:
        out["aggregation_period"] = data["AggregationPeriod"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
