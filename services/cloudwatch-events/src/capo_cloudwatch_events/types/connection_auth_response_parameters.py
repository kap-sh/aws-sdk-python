"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionAuthResponseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_api_key_auth_response_parameters
    import capo_cloudwatch_events.types.connection_basic_auth_response_parameters
    import capo_cloudwatch_events.types.connection_http_parameters
    import capo_cloudwatch_events.types.connection_o_auth_response_parameters


class ConnectionAuthResponseParameters(TypedDict, closed=True):
    basic_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_basic_auth_response_parameters.ConnectionBasicAuthResponseParameters"
    ]
    """<p>The authorization parameters for Basic authorization.</p>"""
    o_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_o_auth_response_parameters.ConnectionOAuthResponseParameters"
    ]
    """<p>The OAuth parameters to use for authorization.</p>"""
    api_key_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_api_key_auth_response_parameters.ConnectionApiKeyAuthResponseParameters"
    ]
    """<p>The API Key parameters to use for authorization.</p>"""
    invocation_http_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>Additional parameters for the connection that are passed through with every invocation to the HTTP endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAuthResponseParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import capo_cloudwatch_events.types.connection_basic_auth_response_parameters

        out["BasicAuthParameters"] = (
            capo_cloudwatch_events.types.connection_basic_auth_response_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_cloudwatch_events.types.connection_o_auth_response_parameters

        out["OAuthParameters"] = (
            capo_cloudwatch_events.types.connection_o_auth_response_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_cloudwatch_events.types.connection_api_key_auth_response_parameters

        out["ApiKeyAuthParameters"] = (
            capo_cloudwatch_events.types.connection_api_key_auth_response_parameters.serialize_aws_json_1_1(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["InvocationHttpParameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.serialize_aws_json_1_1(
                value["invocation_http_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAuthResponseParameters:
    out: ConnectionAuthResponseParameters = {}  # type: ignore[typeddict-item]
    if "BasicAuthParameters" in data:
        import capo_cloudwatch_events.types.connection_basic_auth_response_parameters

        out["basic_auth_parameters"] = (
            capo_cloudwatch_events.types.connection_basic_auth_response_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if "OAuthParameters" in data:
        import capo_cloudwatch_events.types.connection_o_auth_response_parameters

        out["o_auth_parameters"] = (
            capo_cloudwatch_events.types.connection_o_auth_response_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if "ApiKeyAuthParameters" in data:
        import capo_cloudwatch_events.types.connection_api_key_auth_response_parameters

        out["api_key_auth_parameters"] = (
            capo_cloudwatch_events.types.connection_api_key_auth_response_parameters.deserialize_aws_json_1_1(
                data["ApiKeyAuthParameters"]
            )
        )
    if "InvocationHttpParameters" in data:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["InvocationHttpParameters"]
            )
        )
    return out
