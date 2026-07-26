"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetQueryResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message
    import capo_cloudtrail.types.pagination_token
    import capo_cloudtrail.types.query_result_rows
    import capo_cloudtrail.types.query_statistics
    import capo_cloudtrail.types.query_status


class GetQueryResultsResponse(TypedDict, closed=True):
    query_status: NotRequired["capo_cloudtrail.types.query_status.QueryStatus"]
    """<p>The status of the query. Values include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code>.</p>"""
    query_statistics: NotRequired[
        "capo_cloudtrail.types.query_statistics.QueryStatistics"
    ]
    """<p>Shows the count of query results.</p>"""
    query_result_rows: NotRequired[
        "capo_cloudtrail.types.query_result_rows.QueryResultRows"
    ]
    """<p>Contains the individual event results of the query.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of query results.</p>"""
    error_message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>The error message returned if a query failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsResponse) -> dict:
    out: dict = {}
    if "query_status" in value:
        import capo_cloudtrail.types.query_status

        out["QueryStatus"] = capo_cloudtrail.types.query_status.serialize_aws_json_1_1(
            value["query_status"]
        )
    if "query_statistics" in value:
        import capo_cloudtrail.types.query_statistics

        out["QueryStatistics"] = (
            capo_cloudtrail.types.query_statistics.serialize_aws_json_1_1(
                value["query_statistics"]
            )
        )
    if "query_result_rows" in value:
        import capo_cloudtrail.types.query_result_rows

        out["QueryResultRows"] = (
            capo_cloudtrail.types.query_result_rows.serialize_aws_json_1_1(
                value["query_result_rows"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsResponse:
    out: GetQueryResultsResponse = {}  # type: ignore[typeddict-item]
    if "QueryStatus" in data:
        import capo_cloudtrail.types.query_status

        out["query_status"] = (
            capo_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    if "QueryStatistics" in data:
        import capo_cloudtrail.types.query_statistics

        out["query_statistics"] = (
            capo_cloudtrail.types.query_statistics.deserialize_aws_json_1_1(
                data["QueryStatistics"]
            )
        )
    if "QueryResultRows" in data:
        import capo_cloudtrail.types.query_result_rows

        out["query_result_rows"] = (
            capo_cloudtrail.types.query_result_rows.deserialize_aws_json_1_1(
                data["QueryResultRows"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
