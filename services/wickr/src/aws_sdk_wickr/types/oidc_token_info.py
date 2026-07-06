"""Generated from Smithy shape ``com.amazonaws.wickr#OidcTokenInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class OidcTokenInfo(TypedDict, closed=True):
    code_verifier: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The PKCE (Proof Key for Code Exchange) code verifier, a cryptographically random string used to enhance security in the OAuth flow.</p>"""
    code_challenge: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The PKCE code challenge, a transformed version of the code verifier sent during the authorization request for verification.</p>"""
    access_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OAuth access token that can be used to access protected resources on behalf of the authenticated user.</p>"""
    id_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OpenID Connect ID token containing user identity information and authentication context as a signed JWT.</p>"""
    refresh_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OAuth refresh token that can be used to obtain new access tokens without requiring the user to re-authenticate.</p>"""
    token_type: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The type of access token issued, typically 'Bearer', which indicates how the token should be used in API requests.</p>"""
    expires_in: NotRequired["int"]
    """<p>The lifetime of the access token in seconds, indicating when the token will expire and need to be refreshed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OidcTokenInfo) -> dict:
    out: dict = {}
    if "code_verifier" in value:
        out["codeVerifier"] = value["code_verifier"]
    if "code_challenge" in value:
        out["codeChallenge"] = value["code_challenge"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "id_token" in value:
        out["idToken"] = value["id_token"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "token_type" in value:
        out["tokenType"] = value["token_type"]
    if "expires_in" in value:
        out["expiresIn"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> OidcTokenInfo:
    out: OidcTokenInfo = {}  # type: ignore[typeddict-item]
    if "codeVerifier" in data:
        out["code_verifier"] = data["codeVerifier"]
    if "codeChallenge" in data:
        out["code_challenge"] = data["codeChallenge"]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    if "idToken" in data:
        out["id_token"] = data["idToken"]
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    if "tokenType" in data:
        out["token_type"] = data["tokenType"]
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    return out
