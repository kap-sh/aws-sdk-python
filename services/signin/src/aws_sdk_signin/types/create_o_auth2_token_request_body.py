"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenRequestBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.authorization_code
    import aws_sdk_signin.types.client_id
    import aws_sdk_signin.types.code_verifier
    import aws_sdk_signin.types.grant_type
    import aws_sdk_signin.types.redirect_uri
    import aws_sdk_signin.types.refresh_token


class CreateOAuth2TokenRequestBody(TypedDict, closed=True):
    client_id: "aws_sdk_signin.types.client_id.ClientId"
    """The client identifier (ARN) used during Sign-In onboarding Required for both authorization code and refresh token flows"""
    grant_type: "aws_sdk_signin.types.grant_type.GrantType"
    r"""OAuth 2.0 grant type - determines which flow is used Must be \"authorization_code\" or \"refresh_token\""""
    code: NotRequired["aws_sdk_signin.types.authorization_code.AuthorizationCode"]
    """The authorization code received from /v1/authorize Required only when grant_type=authorization_code"""
    redirect_uri: NotRequired["aws_sdk_signin.types.redirect_uri.RedirectUri"]
    """The redirect URI that must match the original authorization request Required only when grant_type=authorization_code"""
    code_verifier: NotRequired["aws_sdk_signin.types.code_verifier.CodeVerifier"]
    """PKCE code verifier to prove possession of the original code challenge Required only when grant_type=authorization_code"""
    refresh_token: NotRequired["aws_sdk_signin.types.refresh_token.RefreshToken"]
    """The refresh token returned from auth_code redemption Required only when grant_type=refresh_token"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenRequestBody) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["grantType"] = value["grant_type"]
    if "code" in value:
        out["code"] = value["code"]
    if "redirect_uri" in value:
        out["redirectUri"] = value["redirect_uri"]
    if "code_verifier" in value:
        out["codeVerifier"] = value["code_verifier"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenRequestBody:
    out: CreateOAuth2TokenRequestBody = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("CreateOAuth2TokenRequestBody.client_id required")
    if "grantType" in data:
        out["grant_type"] = data["grantType"]
    else:
        raise DeserializationError("CreateOAuth2TokenRequestBody.grant_type required")
    if "code" in data:
        out["code"] = data["code"]
    if "redirectUri" in data:
        out["redirect_uri"] = data["redirectUri"]
    if "codeVerifier" in data:
        out["code_verifier"] = data["codeVerifier"]
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    return out
