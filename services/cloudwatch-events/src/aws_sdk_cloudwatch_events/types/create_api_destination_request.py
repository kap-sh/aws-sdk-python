"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.api_destination_description
    import aws_sdk_cloudwatch_events.types.api_destination_http_method
    import aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second
    import aws_sdk_cloudwatch_events.types.api_destination_name
    import aws_sdk_cloudwatch_events.types.connection_arn
    import aws_sdk_cloudwatch_events.types.https_endpoint


class CreateApiDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    """<p>The name for the API destination to create.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_description.ApiDestinationDescription"
    ]
    """<p>A description for the API destination to create.</p>"""
    connection_arn: "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn"
    """<p>The ARN of the connection to use for the API destination. The destination endpoint must support the authorization type specified for the connection.</p>"""
    invocation_endpoint: "aws_sdk_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    """<p>The URL to the HTTP invocation endpoint for the API destination.</p>"""
    http_method: "aws_sdk_cloudwatch_events.types.api_destination_http_method.ApiDestinationHttpMethod"
    """<p>The method to use for the request to the HTTP invocation endpoint.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of requests per second to send to the HTTP invocation endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ConnectionArn"] = value["connection_arn"]
    out["InvocationEndpoint"] = value["invocation_endpoint"]
    import aws_sdk_cloudwatch_events.types.api_destination_http_method

    out["HttpMethod"] = (
        aws_sdk_cloudwatch_events.types.api_destination_http_method.serialize_aws_json_1_1(
            value["http_method"]
        )
    )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApiDestinationRequest:
    out: CreateApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApiDestinationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError(
            "CreateApiDestinationRequest.connection_arn required"
        )
    if "InvocationEndpoint" in data:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    else:
        raise DeserializationError(
            "CreateApiDestinationRequest.invocation_endpoint required"
        )
    if "HttpMethod" in data:
        import aws_sdk_cloudwatch_events.types.api_destination_http_method

        out["http_method"] = (
            aws_sdk_cloudwatch_events.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    else:
        raise DeserializationError("CreateApiDestinationRequest.http_method required")
    if "InvocationRateLimitPerSecond" in data:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    return out
