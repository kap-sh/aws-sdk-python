"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeApiDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.api_destination_arn
    import capo_eventbridge.types.api_destination_description
    import capo_eventbridge.types.api_destination_http_method
    import capo_eventbridge.types.api_destination_invocation_rate_limit_per_second
    import capo_eventbridge.types.api_destination_name
    import capo_eventbridge.types.api_destination_state
    import capo_eventbridge.types.connection_arn
    import capo_eventbridge.types.https_endpoint
    import capo_eventbridge.types.timestamp


class DescribeApiDestinationResponse(TypedDict, closed=True):
    api_destination_arn: NotRequired[
        "capo_eventbridge.types.api_destination_arn.ApiDestinationArn"
    ]
    """<p>The ARN of the API destination retrieved.</p>"""
    name: NotRequired["capo_eventbridge.types.api_destination_name.ApiDestinationName"]
    """<p>The name of the API destination retrieved.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.api_destination_description.ApiDestinationDescription"
    ]
    """<p>The description for the API destination retrieved.</p>"""
    api_destination_state: NotRequired[
        "capo_eventbridge.types.api_destination_state.ApiDestinationState"
    ]
    """<p>The state of the API destination retrieved.</p>"""
    connection_arn: NotRequired["capo_eventbridge.types.connection_arn.ConnectionArn"]
    """<p>The ARN of the connection specified for the API destination retrieved.</p>"""
    invocation_endpoint: NotRequired[
        "capo_eventbridge.types.https_endpoint.HttpsEndpoint"
    ]
    """<p>The URL to use to connect to the HTTP endpoint.</p>"""
    http_method: NotRequired[
        "capo_eventbridge.types.api_destination_http_method.ApiDestinationHttpMethod"
    ]
    """<p>The method to use to connect to the HTTP endpoint.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "capo_eventbridge.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of invocations per second to specified for the API destination. Note that if you set the invocation rate maximum to a value lower the rate necessary to send all events received on to the destination HTTP endpoint, some events may not be delivered within the 24-hour retry window. If you plan to set the rate lower than the rate necessary to deliver all events, consider using a dead-letter queue to catch events that are not delivered within 24 hours.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the API destination was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the API destination was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApiDestinationResponse) -> dict:
    out: dict = {}
    if "api_destination_arn" in value:
        out["ApiDestinationArn"] = value["api_destination_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "api_destination_state" in value:
        import capo_eventbridge.types.api_destination_state

        out["ApiDestinationState"] = (
            capo_eventbridge.types.api_destination_state.serialize_aws_json_1_1(
                value["api_destination_state"]
            )
        )
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "invocation_endpoint" in value:
        out["InvocationEndpoint"] = value["invocation_endpoint"]
    if "http_method" in value:
        import capo_eventbridge.types.api_destination_http_method

        out["HttpMethod"] = (
            capo_eventbridge.types.api_destination_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApiDestinationResponse:
    out: DescribeApiDestinationResponse = {}  # type: ignore[typeddict-item]
    if "ApiDestinationArn" in data:
        out["api_destination_arn"] = data["ApiDestinationArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApiDestinationState" in data:
        import capo_eventbridge.types.api_destination_state

        out["api_destination_state"] = (
            capo_eventbridge.types.api_destination_state.deserialize_aws_json_1_1(
                data["ApiDestinationState"]
            )
        )
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "InvocationEndpoint" in data:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    if "HttpMethod" in data:
        import capo_eventbridge.types.api_destination_http_method

        out["http_method"] = (
            capo_eventbridge.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    if "InvocationRateLimitPerSecond" in data:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    if "CreationTime" in data:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
