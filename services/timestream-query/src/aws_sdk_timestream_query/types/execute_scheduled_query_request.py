"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ExecuteScheduledQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.client_token
    import aws_sdk_timestream_query.types.scheduled_query_insights
    import aws_sdk_timestream_query.types.time


class ExecuteScheduledQueryRequest(TypedDict):
    scheduled_query_arn: (
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>ARN of the scheduled query.</p>"""
    invocation_time: "aws_sdk_timestream_query.types.time.Time"
    """<p>The timestamp in UTC. Query will be run as if it was invoked at this timestamp. </p>"""
    client_token: NotRequired["aws_sdk_timestream_query.types.client_token.ClientToken"]
    """<p>Not used. </p>"""
    query_insights: NotRequired[
        "aws_sdk_timestream_query.types.scheduled_query_insights.ScheduledQueryInsights"
    ]
    """<p>Encapsulates settings for enabling <code>QueryInsights</code>.</p> <p>Enabling <code>QueryInsights</code> returns insights and metrics as a part of the Amazon SNS notification for the query that you executed. You can use <code>QueryInsights</code> to tune your query performance and cost.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    import aws_sdk_timestream_query.types.time

    out["InvocationTime"] = aws_sdk_timestream_query.types.time.serialize_aws_json_1_0(
        value["invocation_time"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "query_insights" in value:
        import aws_sdk_timestream_query.types.scheduled_query_insights

        out["QueryInsights"] = (
            aws_sdk_timestream_query.types.scheduled_query_insights.serialize_aws_json_1_0(
                value["query_insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteScheduledQueryRequest:
    out: ExecuteScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "ScheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        raise DeserializationError(
            "ExecuteScheduledQueryRequest.scheduled_query_arn required"
        )
    if "InvocationTime" in data:
        import aws_sdk_timestream_query.types.time

        out["invocation_time"] = (
            aws_sdk_timestream_query.types.time.deserialize_aws_json_1_0(
                data["InvocationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ExecuteScheduledQueryRequest.invocation_time required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "QueryInsights" in data:
        import aws_sdk_timestream_query.types.scheduled_query_insights

        out["query_insights"] = (
            aws_sdk_timestream_query.types.scheduled_query_insights.deserialize_aws_json_1_0(
                data["QueryInsights"]
            )
        )
    return out
