"""Generated from Smithy shape ``com.amazonaws.appflow#PardotConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.access_token
    import aws_sdk_appflow.types.client_credentials_arn
    import aws_sdk_appflow.types.connector_o_auth_request
    import aws_sdk_appflow.types.refresh_token


class PardotConnectorProfileCredentials(TypedDict, closed=True):
    access_token: NotRequired["aws_sdk_appflow.types.access_token.AccessToken"]
    """<p>The credentials used to access protected Salesforce Pardot resources.</p>"""
    refresh_token: NotRequired["aws_sdk_appflow.types.refresh_token.RefreshToken"]
    """<p>The credentials used to acquire new access tokens.</p>"""
    o_auth_request: NotRequired[
        "aws_sdk_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    client_credentials_arn: NotRequired[
        "aws_sdk_appflow.types.client_credentials_arn.ClientCredentialsArn"
    ]
    """<p>The secret manager ARN, which contains the client ID and client secret of the connected app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PardotConnectorProfileCredentials) -> dict:
    out: dict = {}
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
    if "client_credentials_arn" in value:
        out["clientCredentialsArn"] = value["client_credentials_arn"]
    return out


def deserialize_json(data: dict) -> PardotConnectorProfileCredentials:
    out: PardotConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
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
    if "clientCredentialsArn" in data:
        out["client_credentials_arn"] = data["clientCredentialsArn"]
    return out
