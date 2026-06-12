"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionAuthRequestParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_http_parameters
    import aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters
    import aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters
    import aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters


class CreateConnectionAuthRequestParameters(TypedDict):
    basic_auth_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters.CreateConnectionBasicAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionBasicAuthRequestParameters</code> object that contains the Basic authorization parameters to use for the connection.</p>"""
    o_auth_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters.CreateConnectionOAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionOAuthRequestParameters</code> object that contains the OAuth authorization parameters to use for the connection.</p>"""
    api_key_auth_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.CreateConnectionApiKeyAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionApiKeyAuthRequestParameters</code> object that contains the API key authorization parameters to use for the connection.</p>"""
    invocation_http_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>A <code>ConnectionHttpParameters</code> object that contains the API key authorization parameters to use for the connection. Note that if you include additional parameters for the target of a rule via <code>HttpParameters</code>, including query strings, the parameters added for the connection take precedence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionAuthRequestParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters

        out["BasicAuthParameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters

        out["OAuthParameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters

        out["ApiKeyAuthParameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.serialize_aws_json_1_1(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import aws_sdk_cloudwatch_events.types.connection_http_parameters

        out["InvocationHttpParameters"] = (
            aws_sdk_cloudwatch_events.types.connection_http_parameters.serialize_aws_json_1_1(
                value["invocation_http_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionAuthRequestParameters:
    out: CreateConnectionAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if "BasicAuthParameters" in data:
        import aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_basic_auth_request_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if "OAuthParameters" in data:
        import aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_o_auth_request_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if "ApiKeyAuthParameters" in data:
        import aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.deserialize_aws_json_1_1(
                data["ApiKeyAuthParameters"]
            )
        )
    if "InvocationHttpParameters" in data:
        import aws_sdk_cloudwatch_events.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            aws_sdk_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["InvocationHttpParameters"]
            )
        )
    return out
