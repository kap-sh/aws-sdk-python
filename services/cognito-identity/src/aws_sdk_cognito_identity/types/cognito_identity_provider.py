"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#CognitoIdentityProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.cognito_identity_provider_client_id
    import aws_sdk_cognito_identity.types.cognito_identity_provider_name
    import aws_sdk_cognito_identity.types.cognito_identity_provider_token_check


class CognitoIdentityProvider(TypedDict):
    provider_name: NotRequired[
        "aws_sdk_cognito_identity.types.cognito_identity_provider_name.CognitoIdentityProviderName"
    ]
    """<p>The provider name for an Amazon Cognito user pool. For example, <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789</code>.</p>"""
    client_id: NotRequired[
        "aws_sdk_cognito_identity.types.cognito_identity_provider_client_id.CognitoIdentityProviderClientId"
    ]
    """<p>The client ID for the Amazon Cognito user pool.</p>"""
    server_side_token_check: NotRequired[
        "aws_sdk_cognito_identity.types.cognito_identity_provider_token_check.CognitoIdentityProviderTokenCheck"
    ]
    """<p>TRUE if server-side token validation is enabled for the identity provider’s token.</p> <p>Once you set <code>ServerSideTokenCheck</code> to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or Amazon Web Services credentials for the user.</p> <p>If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CognitoIdentityProvider) -> dict:
    out: dict = {}
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "server_side_token_check" in value:
        out["ServerSideTokenCheck"] = value["server_side_token_check"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CognitoIdentityProvider:
    out: CognitoIdentityProvider = {}  # type: ignore[typeddict-item]
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "ServerSideTokenCheck" in data:
        out["server_side_token_check"] = data["ServerSideTokenCheck"]
    return out
