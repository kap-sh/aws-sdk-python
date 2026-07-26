"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryStatisticsForDescribeQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.integer
    import capo_cloudtrail.types.long


class QueryStatisticsForDescribeQuery(TypedDict, closed=True):
    events_matched: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p>The number of events that matched a query.</p>"""
    events_scanned: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p>The number of events that the query scanned in the event data store.</p>"""
    bytes_scanned: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p>The total bytes that the query scanned in the event data store. This value matches the number of bytes for which your account is billed for the query, unless the query is still running.</p>"""
    execution_time_in_millis: NotRequired["capo_cloudtrail.types.integer.Integer"]
    """<p>The query's run time, in milliseconds.</p>"""
    creation_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The creation time of the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStatisticsForDescribeQuery) -> dict:
    out: dict = {}
    if "events_matched" in value:
        out["EventsMatched"] = value["events_matched"]
    if "events_scanned" in value:
        out["EventsScanned"] = value["events_scanned"]
    if "bytes_scanned" in value:
        out["BytesScanned"] = value["bytes_scanned"]
    if "execution_time_in_millis" in value:
        out["ExecutionTimeInMillis"] = value["execution_time_in_millis"]
    if "creation_time" in value:
        import capo_cloudtrail.types.date

        out["CreationTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStatisticsForDescribeQuery:
    out: QueryStatisticsForDescribeQuery = {}  # type: ignore[typeddict-item]
    if "EventsMatched" in data:
        out["events_matched"] = data["EventsMatched"]
    if "EventsScanned" in data:
        out["events_scanned"] = data["EventsScanned"]
    if "BytesScanned" in data:
        out["bytes_scanned"] = data["BytesScanned"]
    if "ExecutionTimeInMillis" in data:
        out["execution_time_in_millis"] = data["ExecutionTimeInMillis"]
    if "CreationTime" in data:
        import capo_cloudtrail.types.date

        out["creation_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
