"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DescribeQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.account_id
    import aws_sdk_cloudtrail.types.delivery_s3_uri
    import aws_sdk_cloudtrail.types.delivery_status
    import aws_sdk_cloudtrail.types.error_message
    import aws_sdk_cloudtrail.types.prompt
    import aws_sdk_cloudtrail.types.query_statement
    import aws_sdk_cloudtrail.types.query_statistics_for_describe_query
    import aws_sdk_cloudtrail.types.query_status
    import aws_sdk_cloudtrail.types.uuid


class DescribeQueryResponse(TypedDict):
    query_id: NotRequired["aws_sdk_cloudtrail.types.uuid.UUID"]
    """<p>The ID of the query.</p>"""
    query_string: NotRequired["aws_sdk_cloudtrail.types.query_statement.QueryStatement"]
    """<p>The SQL code of a query.</p>"""
    query_status: NotRequired["aws_sdk_cloudtrail.types.query_status.QueryStatus"]
    """<p>The status of a query. Values for <code>QueryStatus</code> include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code> </p>"""
    query_statistics: NotRequired[
        "aws_sdk_cloudtrail.types.query_statistics_for_describe_query.QueryStatisticsForDescribeQuery"
    ]
    """<p>Metadata about a query, including the number of events that were matched, the total number of events scanned, the query run time in milliseconds, and the query's creation time.</p>"""
    error_message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>The error message returned if a query failed.</p>"""
    delivery_s3_uri: NotRequired[
        "aws_sdk_cloudtrail.types.delivery_s3_uri.DeliveryS3Uri"
    ]
    """<p>The URI for the S3 bucket where CloudTrail delivered query results, if applicable.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_cloudtrail.types.delivery_status.DeliveryStatus"
    ]
    """<p>The delivery status.</p>"""
    prompt: NotRequired["aws_sdk_cloudtrail.types.prompt.Prompt"]
    """<p> The prompt used for a generated query. For information about generated queries, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html\">Create CloudTrail Lake queries from natural language prompts</a> in the <i>CloudTrail </i> user guide. </p>"""
    event_data_store_owner_account_id: NotRequired[
        "aws_sdk_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryResponse) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "query_status" in value:
        import aws_sdk_cloudtrail.types.query_status

        out["QueryStatus"] = (
            aws_sdk_cloudtrail.types.query_status.serialize_aws_json_1_1(
                value["query_status"]
            )
        )
    if "query_statistics" in value:
        import aws_sdk_cloudtrail.types.query_statistics_for_describe_query

        out["QueryStatistics"] = (
            aws_sdk_cloudtrail.types.query_statistics_for_describe_query.serialize_aws_json_1_1(
                value["query_statistics"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "delivery_s3_uri" in value:
        out["DeliveryS3Uri"] = value["delivery_s3_uri"]
    if "delivery_status" in value:
        import aws_sdk_cloudtrail.types.delivery_status

        out["DeliveryStatus"] = (
            aws_sdk_cloudtrail.types.delivery_status.serialize_aws_json_1_1(
                value["delivery_status"]
            )
        )
    if "prompt" in value:
        out["Prompt"] = value["prompt"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryResponse:
    out: DescribeQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    if "QueryStatus" in data:
        import aws_sdk_cloudtrail.types.query_status

        out["query_status"] = (
            aws_sdk_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    if "QueryStatistics" in data:
        import aws_sdk_cloudtrail.types.query_statistics_for_describe_query

        out["query_statistics"] = (
            aws_sdk_cloudtrail.types.query_statistics_for_describe_query.deserialize_aws_json_1_1(
                data["QueryStatistics"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "DeliveryS3Uri" in data:
        out["delivery_s3_uri"] = data["DeliveryS3Uri"]
    if "DeliveryStatus" in data:
        import aws_sdk_cloudtrail.types.delivery_status

        out["delivery_status"] = (
            aws_sdk_cloudtrail.types.delivery_status.deserialize_aws_json_1_1(
                data["DeliveryStatus"]
            )
        )
    if "Prompt" in data:
        out["prompt"] = data["Prompt"]
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
