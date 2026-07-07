"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.column_info_list
    import aws_sdk_timestream_query.types.pagination_token
    import aws_sdk_timestream_query.types.query_id
    import aws_sdk_timestream_query.types.query_insights_response
    import aws_sdk_timestream_query.types.query_status
    import aws_sdk_timestream_query.types.row_list


class QueryResponse(TypedDict, closed=True):
    query_id: "aws_sdk_timestream_query.types.query_id.QueryId"
    """<p> A unique ID for the given query. </p>"""
    next_token: NotRequired[
        "aws_sdk_timestream_query.types.pagination_token.PaginationToken"
    ]
    """<p> A pagination token that can be used again on a <code>Query</code> call to get the next set of results. </p>"""
    rows: "aws_sdk_timestream_query.types.row_list.RowList"
    """<p> The result set rows returned by the query. </p>"""
    column_info: "aws_sdk_timestream_query.types.column_info_list.ColumnInfoList"
    """<p> The column data types of the returned result set. </p>"""
    query_status: NotRequired["aws_sdk_timestream_query.types.query_status.QueryStatus"]
    """<p>Information about the status of the query, including progress and bytes scanned.</p>"""
    query_insights_response: NotRequired[
        "aws_sdk_timestream_query.types.query_insights_response.QueryInsightsResponse"
    ]
    """<p>Encapsulates <code>QueryInsights</code> containing insights and metrics related to the query that you executed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryResponse) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_timestream_query.types.row_list

    out["Rows"] = aws_sdk_timestream_query.types.row_list.serialize_aws_json_1_0(
        value["rows"]
    )
    import aws_sdk_timestream_query.types.column_info_list

    out["ColumnInfo"] = (
        aws_sdk_timestream_query.types.column_info_list.serialize_aws_json_1_0(
            value["column_info"]
        )
    )
    if "query_status" in value:
        import aws_sdk_timestream_query.types.query_status

        out["QueryStatus"] = (
            aws_sdk_timestream_query.types.query_status.serialize_aws_json_1_0(
                value["query_status"]
            )
        )
    if "query_insights_response" in value:
        import aws_sdk_timestream_query.types.query_insights_response

        out["QueryInsightsResponse"] = (
            aws_sdk_timestream_query.types.query_insights_response.serialize_aws_json_1_0(
                value["query_insights_response"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryResponse:
    out: QueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("QueryResponse.query_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Rows" in data:
        import aws_sdk_timestream_query.types.row_list

        out["rows"] = aws_sdk_timestream_query.types.row_list.deserialize_aws_json_1_0(
            data["Rows"]
        )
    else:
        raise DeserializationError("QueryResponse.rows required")
    if "ColumnInfo" in data:
        import aws_sdk_timestream_query.types.column_info_list

        out["column_info"] = (
            aws_sdk_timestream_query.types.column_info_list.deserialize_aws_json_1_0(
                data["ColumnInfo"]
            )
        )
    else:
        raise DeserializationError("QueryResponse.column_info required")
    if "QueryStatus" in data:
        import aws_sdk_timestream_query.types.query_status

        out["query_status"] = (
            aws_sdk_timestream_query.types.query_status.deserialize_aws_json_1_0(
                data["QueryStatus"]
            )
        )
    if "QueryInsightsResponse" in data:
        import aws_sdk_timestream_query.types.query_insights_response

        out["query_insights_response"] = (
            aws_sdk_timestream_query.types.query_insights_response.deserialize_aws_json_1_0(
                data["QueryInsightsResponse"]
            )
        )
    return out
