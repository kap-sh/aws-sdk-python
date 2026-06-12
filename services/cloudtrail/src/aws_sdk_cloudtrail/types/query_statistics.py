"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.integer
    import aws_sdk_cloudtrail.types.long


class QueryStatistics(TypedDict):
    results_count: NotRequired["aws_sdk_cloudtrail.types.integer.Integer"]
    """<p>The number of results returned.</p>"""
    total_results_count: NotRequired["aws_sdk_cloudtrail.types.integer.Integer"]
    """<p>The total number of results returned by a query.</p>"""
    bytes_scanned: NotRequired["aws_sdk_cloudtrail.types.long.Long"]
    """<p>The total bytes that the query scanned in the event data store. This value matches the number of bytes for which your account is billed for the query, unless the query is still running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStatistics) -> dict:
    out: dict = {}
    if "results_count" in value:
        out["ResultsCount"] = value["results_count"]
    if "total_results_count" in value:
        out["TotalResultsCount"] = value["total_results_count"]
    if "bytes_scanned" in value:
        out["BytesScanned"] = value["bytes_scanned"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if "ResultsCount" in data:
        out["results_count"] = data["ResultsCount"]
    if "TotalResultsCount" in data:
        out["total_results_count"] = data["TotalResultsCount"]
    if "BytesScanned" in data:
        out["bytes_scanned"] = data["BytesScanned"]
    return out
