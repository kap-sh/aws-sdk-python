"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateApiDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.api_destination_description
    import aws_sdk_eventbridge.types.api_destination_http_method
    import aws_sdk_eventbridge.types.api_destination_invocation_rate_limit_per_second
    import aws_sdk_eventbridge.types.api_destination_name
    import aws_sdk_eventbridge.types.connection_arn
    import aws_sdk_eventbridge.types.https_endpoint


class UpdateApiDestinationRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.api_destination_name.ApiDestinationName"
    """<p>The name of the API destination to update.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_description.ApiDestinationDescription"
    ]
    """<p>The name of the API destination to update.</p>"""
    connection_arn: NotRequired[
        "aws_sdk_eventbridge.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection to use for the API destination.</p>"""
    invocation_endpoint: NotRequired[
        "aws_sdk_eventbridge.types.https_endpoint.HttpsEndpoint"
    ]
    """<p>The URL to the endpoint to use for the API destination.</p>"""
    http_method: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_http_method.ApiDestinationHttpMethod"
    ]
    """<p>The method to use for the API destination.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of invocations per second to send to the API destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "invocation_endpoint" in value:
        out["InvocationEndpoint"] = value["invocation_endpoint"]
    if "http_method" in value:
        import aws_sdk_eventbridge.types.api_destination_http_method

        out["HttpMethod"] = (
            aws_sdk_eventbridge.types.api_destination_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApiDestinationRequest:
    out: UpdateApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateApiDestinationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "InvocationEndpoint" in data:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    if "HttpMethod" in data:
        import aws_sdk_eventbridge.types.api_destination_http_method

        out["http_method"] = (
            aws_sdk_eventbridge.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    if "InvocationRateLimitPerSecond" in data:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    return out
