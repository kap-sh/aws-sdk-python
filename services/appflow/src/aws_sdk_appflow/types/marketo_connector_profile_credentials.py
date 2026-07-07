"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.access_token
    import aws_sdk_appflow.types.client_id
    import aws_sdk_appflow.types.client_secret
    import aws_sdk_appflow.types.connector_o_auth_request


class MarketoConnectorProfileCredentials(TypedDict, closed=True):
    client_id: "aws_sdk_appflow.types.client_id.ClientId"
    """<p> The identifier for the desired client. </p>"""
    client_secret: "aws_sdk_appflow.types.client_secret.ClientSecret"
    """<p> The client secret used by the OAuth client to authenticate to the authorization server. </p>"""
    access_token: NotRequired["aws_sdk_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Marketo resources. </p>"""
    o_auth_request: NotRequired[
        "aws_sdk_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    """<p> The OAuth requirement needed to request security tokens from the connector endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketoConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "o_auth_request" in value:
        import aws_sdk_appflow.types.connector_o_auth_request

        out["oAuthRequest"] = (
            aws_sdk_appflow.types.connector_o_auth_request.serialize_json(
                value["o_auth_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> MarketoConnectorProfileCredentials:
    out: MarketoConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "MarketoConnectorProfileCredentials.client_id required"
        )
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "MarketoConnectorProfileCredentials.client_secret required"
        )
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    if "oAuthRequest" in data:
        import aws_sdk_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            aws_sdk_appflow.types.connector_o_auth_request.deserialize_json(
                data["oAuthRequest"]
            )
        )
    return out
