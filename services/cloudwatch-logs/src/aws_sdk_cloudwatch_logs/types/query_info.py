"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.bytes_scanned_value
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.query_duration
    import aws_sdk_cloudwatch_logs.types.query_id
    import aws_sdk_cloudwatch_logs.types.query_language
    import aws_sdk_cloudwatch_logs.types.query_status
    import aws_sdk_cloudwatch_logs.types.query_string
    import aws_sdk_cloudwatch_logs.types.timestamp
    import aws_sdk_cloudwatch_logs.types.user_identity


class QueryInfo(TypedDict):
    query_language: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    r"""<p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html\">Supported query languages</a>.</p>"""
    query_id: NotRequired["aws_sdk_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The unique ID number of this query.</p>"""
    query_string: NotRequired["aws_sdk_cloudwatch_logs.types.query_string.QueryString"]
    """<p>The query string used in this query.</p>"""
    status: NotRequired["aws_sdk_cloudwatch_logs.types.query_status.QueryStatus"]
    """<p>The status of this query. Possible values are <code>Cancelled</code>, <code>Complete</code>, <code>Failed</code>, <code>Running</code>, <code>Scheduled</code>, and <code>Unknown</code>.</p>"""
    create_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this query was created.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group scanned by this query.</p>"""
    query_duration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_duration.QueryDuration"
    ]
    """<p>The duration in milliseconds that the query took to execute.</p>"""
    bytes_scanned: NotRequired[
        "aws_sdk_cloudwatch_logs.types.bytes_scanned_value.BytesScannedValue"
    ]
    """<p>The total number of bytes scanned by the query. This indicates the cost associated with the query.</p>"""
    user_identity: NotRequired[
        "aws_sdk_cloudwatch_logs.types.user_identity.UserIdentity"
    ]
    """<p>The ARN of the user who ran the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryInfo) -> dict:
    out: dict = {}
    if "query_language" in value:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "create_time" in value:
        out["createTime"] = value["create_time"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "query_duration" in value:
        out["queryDuration"] = value["query_duration"]
    if "bytes_scanned" in value:
        out["bytesScanned"] = value["bytes_scanned"]
    if "user_identity" in value:
        out["userIdentity"] = value["user_identity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryInfo:
    out: QueryInfo = {}  # type: ignore[typeddict-item]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "queryDuration" in data:
        out["query_duration"] = data["queryDuration"]
    if "bytesScanned" in data:
        out["bytes_scanned"] = data["bytesScanned"]
    if "userIdentity" in data:
        out["user_identity"] = data["userIdentity"]
    return out
