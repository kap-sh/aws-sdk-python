"""Generated from Smithy shape ``com.amazonaws.ssooidc#CreateTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.access_token
    import aws_sdk_sso_oidc.types.expiration_in_seconds
    import aws_sdk_sso_oidc.types.id_token
    import aws_sdk_sso_oidc.types.refresh_token
    import aws_sdk_sso_oidc.types.token_type


class CreateTokenResponse(TypedDict):
    access_token: NotRequired["aws_sdk_sso_oidc.types.access_token.AccessToken"]
    """<p>A bearer token to access Amazon Web Services accounts and applications assigned to a user.</p>"""
    token_type: NotRequired["aws_sdk_sso_oidc.types.token_type.TokenType"]
    """<p>Used to notify the client that the returned token is an access token. The supported token type is <code>Bearer</code>.</p>"""
    expires_in: "aws_sdk_sso_oidc.types.expiration_in_seconds.ExpirationInSeconds"
    """<p>Indicates the time in seconds when an access token will expire.</p>"""
    refresh_token: NotRequired["aws_sdk_sso_oidc.types.refresh_token.RefreshToken"]
    """<p>A token that, if present, can be used to refresh a previously issued access token that might have expired.</p> <p>For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html\">IAM Identity Center OIDC API Reference</a>.</p>"""
    id_token: NotRequired["aws_sdk_sso_oidc.types.id_token.IdToken"]
    """<p>The <code>idToken</code> is not implemented or supported. For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html\">IAM Identity Center OIDC API Reference</a>.</p> <p>A JSON Web Token (JWT) that identifies who is associated with the issued access token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTokenResponse) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "token_type" in value:
        out["tokenType"] = value["token_type"]
    out["expiresIn"] = value.get("expires_in", 0)
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["idToken"] = value["id_token"]
    return out


def deserialize_json(data: dict) -> CreateTokenResponse:
    out: CreateTokenResponse = {}  # type: ignore[typeddict-item]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    if "tokenType" in data:
        out["token_type"] = data["tokenType"]
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    else:
        out["expires_in"] = 0
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    if "idToken" in data:
        out["id_token"] = data["idToken"]
    return out
