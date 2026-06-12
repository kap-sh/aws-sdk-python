"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionOAuthRequestParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_http_parameters
    import aws_sdk_cloudwatch_events.types.connection_o_auth_http_method
    import aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters
    import aws_sdk_cloudwatch_events.types.https_endpoint


class CreateConnectionOAuthRequestParameters(TypedDict):
    client_parameters: "aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.CreateConnectionOAuthClientRequestParameters"
    """<p>A <code>CreateConnectionOAuthClientRequestParameters</code> object that contains the client parameters for OAuth authorization.</p>"""
    authorization_endpoint: (
        "aws_sdk_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    )
    """<p>The URL to the authorization endpoint when OAuth is specified as the authorization type.</p>"""
    http_method: "aws_sdk_cloudwatch_events.types.connection_o_auth_http_method.ConnectionOAuthHttpMethod"
    """<p>The method to use for the authorization request.</p>"""
    o_auth_http_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>A <code>ConnectionHttpParameters</code> object that contains details about the additional parameters to use for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionOAuthRequestParameters) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters

    out["ClientParameters"] = (
        aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.serialize_aws_json_1_1(
            value["client_parameters"]
        )
    )
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    import aws_sdk_cloudwatch_events.types.connection_o_auth_http_method

    out["HttpMethod"] = (
        aws_sdk_cloudwatch_events.types.connection_o_auth_http_method.serialize_aws_json_1_1(
            value["http_method"]
        )
    )
    if "o_auth_http_parameters" in value:
        import aws_sdk_cloudwatch_events.types.connection_http_parameters

        out["OAuthHttpParameters"] = (
            aws_sdk_cloudwatch_events.types.connection_http_parameters.serialize_aws_json_1_1(
                value["o_auth_http_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionOAuthRequestParameters:
    out: CreateConnectionOAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if "ClientParameters" in data:
        import aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters

        out["client_parameters"] = (
            aws_sdk_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.deserialize_aws_json_1_1(
                data["ClientParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionOAuthRequestParameters.client_parameters required"
        )
    if "AuthorizationEndpoint" in data:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        raise DeserializationError(
            "CreateConnectionOAuthRequestParameters.authorization_endpoint required"
        )
    if "HttpMethod" in data:
        import aws_sdk_cloudwatch_events.types.connection_o_auth_http_method

        out["http_method"] = (
            aws_sdk_cloudwatch_events.types.connection_o_auth_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionOAuthRequestParameters.http_method required"
        )
    if "OAuthHttpParameters" in data:
        import aws_sdk_cloudwatch_events.types.connection_http_parameters

        out["o_auth_http_parameters"] = (
            aws_sdk_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["OAuthHttpParameters"]
            )
        )
    return out
