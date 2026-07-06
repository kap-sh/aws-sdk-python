"""Generated from Smithy shape ``com.amazonaws.appflow#GoogleAnalyticsConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.access_token
    import aws_sdk_appflow.types.client_id
    import aws_sdk_appflow.types.client_secret
    import aws_sdk_appflow.types.connector_o_auth_request
    import aws_sdk_appflow.types.refresh_token


class GoogleAnalyticsConnectorProfileCredentials(TypedDict, closed=True):
    client_id: "aws_sdk_appflow.types.client_id.ClientId"
    """<p> The identifier for the desired client. </p>"""
    client_secret: "aws_sdk_appflow.types.client_secret.ClientSecret"
    """<p> The client secret used by the OAuth client to authenticate to the authorization server. </p>"""
    access_token: NotRequired["aws_sdk_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Google Analytics resources. </p>"""
    refresh_token: NotRequired["aws_sdk_appflow.types.refresh_token.RefreshToken"]
    """<p> The credentials used to acquire new access tokens. This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens. </p>"""
    o_auth_request: NotRequired[
        "aws_sdk_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    """<p> The OAuth requirement needed to request security tokens from the connector endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoogleAnalyticsConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "o_auth_request" in value:
        import aws_sdk_appflow.types.connector_o_auth_request

        out["oAuthRequest"] = (
            aws_sdk_appflow.types.connector_o_auth_request.serialize_json(
                value["o_auth_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> GoogleAnalyticsConnectorProfileCredentials:
    out: GoogleAnalyticsConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "GoogleAnalyticsConnectorProfileCredentials.client_id required"
        )
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "GoogleAnalyticsConnectorProfileCredentials.client_secret required"
        )
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    if "oAuthRequest" in data:
        import aws_sdk_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            aws_sdk_appflow.types.connector_o_auth_request.deserialize_json(
                data["oAuthRequest"]
            )
        )
    return out
