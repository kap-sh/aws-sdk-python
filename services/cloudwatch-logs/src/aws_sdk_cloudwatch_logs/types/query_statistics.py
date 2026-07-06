"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.stats_value


class QueryStatistics(TypedDict, closed=True):
    records_matched: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The number of log events that matched the query string.</p>"""
    records_scanned: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The total number of log events scanned during the query.</p>"""
    estimated_records_skipped: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    r"""<p>An estimate of the number of log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html\">PutIndexPolicy</a>.</p>"""
    bytes_scanned: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The total number of bytes in the log events scanned during the query.</p>"""
    estimated_bytes_skipped: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    r"""<p>An estimate of the number of bytes in the log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html\">PutIndexPolicy</a>.</p>"""
    log_groups_scanned: "aws_sdk_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The number of log groups that were scanned by this query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStatistics) -> dict:
    out: dict = {}
    out["recordsMatched"] = value.get("records_matched", 0)
    out["recordsScanned"] = value.get("records_scanned", 0)
    out["estimatedRecordsSkipped"] = value.get("estimated_records_skipped", 0)
    out["bytesScanned"] = value.get("bytes_scanned", 0)
    out["estimatedBytesSkipped"] = value.get("estimated_bytes_skipped", 0)
    out["logGroupsScanned"] = value.get("log_groups_scanned", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if "recordsMatched" in data:
        out["records_matched"] = data["recordsMatched"]
    else:
        out["records_matched"] = 0
    if "recordsScanned" in data:
        out["records_scanned"] = data["recordsScanned"]
    else:
        out["records_scanned"] = 0
    if "estimatedRecordsSkipped" in data:
        out["estimated_records_skipped"] = data["estimatedRecordsSkipped"]
    else:
        out["estimated_records_skipped"] = 0
    if "bytesScanned" in data:
        out["bytes_scanned"] = data["bytesScanned"]
    else:
        out["bytes_scanned"] = 0
    if "estimatedBytesSkipped" in data:
        out["estimated_bytes_skipped"] = data["estimatedBytesSkipped"]
    else:
        out["estimated_bytes_skipped"] = 0
    if "logGroupsScanned" in data:
        out["log_groups_scanned"] = data["logGroupsScanned"]
    else:
        out["log_groups_scanned"] = 0
    return out
