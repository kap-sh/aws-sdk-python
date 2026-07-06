"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ApiDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.api_destination_arn
    import aws_sdk_cloudwatch_events.types.api_destination_http_method
    import aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second
    import aws_sdk_cloudwatch_events.types.api_destination_name
    import aws_sdk_cloudwatch_events.types.api_destination_state
    import aws_sdk_cloudwatch_events.types.connection_arn
    import aws_sdk_cloudwatch_events.types.https_endpoint
    import aws_sdk_cloudwatch_events.types.timestamp


class ApiDestination(TypedDict, closed=True):
    api_destination_arn: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_arn.ApiDestinationArn"
    ]
    """<p>The ARN of the API destination.</p>"""
    name: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    ]
    """<p>The name of the API destination.</p>"""
    api_destination_state: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_state.ApiDestinationState"
    ]
    """<p>The state of the API destination.</p>"""
    connection_arn: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection specified for the API destination.</p>"""
    invocation_endpoint: NotRequired[
        "aws_sdk_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    ]
    """<p>The URL to the endpoint for the API destination.</p>"""
    http_method: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_http_method.ApiDestinationHttpMethod"
    ]
    """<p>The method to use to connect to the HTTP endpoint.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of invocations per second to send to the HTTP endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the API destination was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_cloudwatch_events.types.timestamp.Timestamp"
    ]
    """<p>A time stamp for the time that the API destination was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiDestination) -> dict:
    out: dict = {}
    if "api_destination_arn" in value:
        out["ApiDestinationArn"] = value["api_destination_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "api_destination_state" in value:
        import aws_sdk_cloudwatch_events.types.api_destination_state

        out["ApiDestinationState"] = (
            aws_sdk_cloudwatch_events.types.api_destination_state.serialize_aws_json_1_1(
                value["api_destination_state"]
            )
        )
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "invocation_endpoint" in value:
        out["InvocationEndpoint"] = value["invocation_endpoint"]
    if "http_method" in value:
        import aws_sdk_cloudwatch_events.types.api_destination_http_method

        out["HttpMethod"] = (
            aws_sdk_cloudwatch_events.types.api_destination_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    if "creation_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApiDestination:
    out: ApiDestination = {}  # type: ignore[typeddict-item]
    if "ApiDestinationArn" in data:
        out["api_destination_arn"] = data["ApiDestinationArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ApiDestinationState" in data:
        import aws_sdk_cloudwatch_events.types.api_destination_state

        out["api_destination_state"] = (
            aws_sdk_cloudwatch_events.types.api_destination_state.deserialize_aws_json_1_1(
                data["ApiDestinationState"]
            )
        )
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "InvocationEndpoint" in data:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    if "HttpMethod" in data:
        import aws_sdk_cloudwatch_events.types.api_destination_http_method

        out["http_method"] = (
            aws_sdk_cloudwatch_events.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    if "InvocationRateLimitPerSecond" in data:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    if "CreationTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
