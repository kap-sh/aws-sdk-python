"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateConnectionAuthRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_http_parameters
    import aws_sdk_eventbridge.types.connectivity_resource_parameters
    import aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters
    import aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters
    import aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters


class UpdateConnectionAuthRequestParameters(TypedDict, closed=True):
    basic_auth_parameters: NotRequired[
        "aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters.UpdateConnectionBasicAuthRequestParameters"
    ]
    """<p>The authorization parameters for Basic authorization.</p>"""
    o_auth_parameters: NotRequired[
        "aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters.UpdateConnectionOAuthRequestParameters"
    ]
    """<p>The authorization parameters for OAuth authorization.</p>"""
    api_key_auth_parameters: NotRequired[
        "aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters.UpdateConnectionApiKeyAuthRequestParameters"
    ]
    """<p>The authorization parameters for API key authorization.</p>"""
    invocation_http_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>The additional parameters to use for the connection.</p>"""
    connectivity_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connectivity_resource_parameters.ConnectivityResourceParameters"
    ]
    r"""<p>If you specify a private OAuth endpoint, the parameters for EventBridge to use when authenticating against the endpoint.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html\">Authorization methods for connections</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionAuthRequestParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters

        out["BasicAuthParameters"] = (
            aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters

        out["OAuthParameters"] = (
            aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters

        out["ApiKeyAuthParameters"] = (
            aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters.serialize_aws_json_1_1(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import aws_sdk_eventbridge.types.connection_http_parameters

        out["InvocationHttpParameters"] = (
            aws_sdk_eventbridge.types.connection_http_parameters.serialize_aws_json_1_1(
                value["invocation_http_parameters"]
            )
        )
    if "connectivity_parameters" in value:
        import aws_sdk_eventbridge.types.connectivity_resource_parameters

        out["ConnectivityParameters"] = (
            aws_sdk_eventbridge.types.connectivity_resource_parameters.serialize_aws_json_1_1(
                value["connectivity_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionAuthRequestParameters:
    out: UpdateConnectionAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if "BasicAuthParameters" in data:
        import aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            aws_sdk_eventbridge.types.update_connection_basic_auth_request_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if "OAuthParameters" in data:
        import aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            aws_sdk_eventbridge.types.update_connection_o_auth_request_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if "ApiKeyAuthParameters" in data:
        import aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            aws_sdk_eventbridge.types.update_connection_api_key_auth_request_parameters.deserialize_aws_json_1_1(
                data["ApiKeyAuthParameters"]
            )
        )
    if "InvocationHttpParameters" in data:
        import aws_sdk_eventbridge.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            aws_sdk_eventbridge.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["InvocationHttpParameters"]
            )
        )
    if "ConnectivityParameters" in data:
        import aws_sdk_eventbridge.types.connectivity_resource_parameters

        out["connectivity_parameters"] = (
            aws_sdk_eventbridge.types.connectivity_resource_parameters.deserialize_aws_json_1_1(
                data["ConnectivityParameters"]
            )
        )
    return out
