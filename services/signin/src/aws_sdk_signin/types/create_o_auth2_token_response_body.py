"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenResponseBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.access_token
    import aws_sdk_signin.types.expires_in
    import aws_sdk_signin.types.id_token
    import aws_sdk_signin.types.refresh_token
    import aws_sdk_signin.types.token_type


class CreateOAuth2TokenResponseBody(TypedDict):
    access_token: "aws_sdk_signin.types.access_token.AccessToken"
    """Scoped-down AWS credentials (15 minute duration) Present for both authorization code redemption and token refresh"""
    token_type: "aws_sdk_signin.types.token_type.TokenType"
    r"""Token type indicating this is AWS SigV4 credentials Value is \"aws_sigv4\" for both flows"""
    expires_in: "aws_sdk_signin.types.expires_in.ExpiresIn"
    """Time to expiry in seconds (maximum 900) Present for both authorization code redemption and token refresh"""
    refresh_token: "aws_sdk_signin.types.refresh_token.RefreshToken"
    """Encrypted refresh token with cnf.jkt (SHA-256 thumbprint of presented jwk) Always present in responses (required for both flows)"""
    id_token: NotRequired["aws_sdk_signin.types.id_token.IdToken"]
    """ID token containing user identity information Present only in authorization code redemption response (grant_type=authorization_code) Not included in token refresh responses"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenResponseBody) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.access_token

    out["accessToken"] = aws_sdk_signin.types.access_token.serialize_json(
        value["access_token"]
    )
    out["tokenType"] = value["token_type"]
    out["expiresIn"] = value["expires_in"]
    out["refreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["idToken"] = value["id_token"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenResponseBody:
    out: CreateOAuth2TokenResponseBody = {}  # type: ignore[typeddict-item]
    if "accessToken" in data:
        import aws_sdk_signin.types.access_token

        out["access_token"] = aws_sdk_signin.types.access_token.deserialize_json(
            data["accessToken"]
        )
    else:
        raise DeserializationError(
            "CreateOAuth2TokenResponseBody.access_token required"
        )
    if "tokenType" in data:
        out["token_type"] = data["tokenType"]
    else:
        raise DeserializationError("CreateOAuth2TokenResponseBody.token_type required")
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    else:
        raise DeserializationError("CreateOAuth2TokenResponseBody.expires_in required")
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    else:
        raise DeserializationError(
            "CreateOAuth2TokenResponseBody.refresh_token required"
        )
    if "idToken" in data:
        out["id_token"] = data["idToken"]
    return out
