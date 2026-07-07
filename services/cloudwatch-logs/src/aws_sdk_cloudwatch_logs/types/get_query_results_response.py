"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetQueryResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.encryption_key
    import aws_sdk_cloudwatch_logs.types.get_query_results_next_token
    import aws_sdk_cloudwatch_logs.types.query_language
    import aws_sdk_cloudwatch_logs.types.query_results
    import aws_sdk_cloudwatch_logs.types.query_statistics
    import aws_sdk_cloudwatch_logs.types.query_status


class GetQueryResultsResponse(TypedDict, closed=True):
    query_language: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    r"""<p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html\">Supported query languages</a>.</p>"""
    results: NotRequired["aws_sdk_cloudwatch_logs.types.query_results.QueryResults"]
    """<p>The log events that matched the query criteria during the most recent time it ran.</p> <p>The <code>results</code> value is an array of arrays. Each log event is one object in the top-level array. Each of these log event objects is an array of <code>field</code>/<code>value</code> pairs.</p>"""
    statistics: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_statistics.QueryStatistics"
    ]
    """<p>Includes the number of log events scanned by the query, the number of log events that matched the query criteria, and the total number of bytes in the scanned log events. These values reflect the full raw results of the query.</p>"""
    status: NotRequired["aws_sdk_cloudwatch_logs.types.query_status.QueryStatus"]
    """<p>The status of the most recent running of the query. Possible values are <code>Cancelled</code>, <code>Complete</code>, <code>Failed</code>, <code>Running</code>, <code>Scheduled</code>, <code>Timeout</code>, and <code>Unknown</code>.</p> <p>Queries time out after 60 minutes of runtime. To avoid having your queries time out, reduce the time range being searched or partition your query into a number of queries.</p>"""
    encryption_key: NotRequired[
        "aws_sdk_cloudwatch_logs.types.encryption_key.EncryptionKey"
    ]
    r"""<p>If you associated an KMS key with the CloudWatch Logs Insights query results in this account, this field displays the ARN of the key that's used to encrypt the query results when <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html\">StartQuery</a> stores them.</p>"""
    next_token: NotRequired[
        "aws_sdk_cloudwatch_logs.types.get_query_results_next_token.GetQueryResultsNextToken"
    ]
    """<p>If there are more log events remaining in the results, the response includes a <code>nextToken</code>. You can use this token in a subsequent <code>GetQueryResults</code> request to get the next set of results. You can retrieve up to 100,000 log event results from a query by paginating with this token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsResponse) -> dict:
    out: dict = {}
    if "query_language" in value:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "results" in value:
        import aws_sdk_cloudwatch_logs.types.query_results

        out["results"] = (
            aws_sdk_cloudwatch_logs.types.query_results.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "statistics" in value:
        import aws_sdk_cloudwatch_logs.types.query_statistics

        out["statistics"] = (
            aws_sdk_cloudwatch_logs.types.query_statistics.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsResponse:
    out: GetQueryResultsResponse = {}  # type: ignore[typeddict-item]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if "results" in data:
        import aws_sdk_cloudwatch_logs.types.query_results

        out["results"] = (
            aws_sdk_cloudwatch_logs.types.query_results.deserialize_aws_json_1_1(
                data["results"]
            )
        )
    if "statistics" in data:
        import aws_sdk_cloudwatch_logs.types.query_statistics

        out["statistics"] = (
            aws_sdk_cloudwatch_logs.types.query_statistics.deserialize_aws_json_1_1(
                data["statistics"]
            )
        )
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
