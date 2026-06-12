"""Generated from Smithy shape ``com.amazonaws.datazone#AuthorizationCodeProperties``."""

from typing import TypedDict
from typing_extensions import NotRequired

class AuthorizationCodeProperties(TypedDict):
    authorization_code: NotRequired["str"]
    """<p>The authorization code of a connection.</p>"""
    redirect_uri: NotRequired["str"]
    """<p>The redirect URI of a connection.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeProperties) -> dict:
    out: dict = {}
    if "authorization_code" in value:
        out["authorizationCode"] = value["authorization_code"]
    if "redirect_uri" in value:
        out["redirectUri"] = value["redirect_uri"]
    return out


def deserialize_json(data: dict) -> AuthorizationCodeProperties:
    out: AuthorizationCodeProperties = {}  # type: ignore[typeddict-item]
    if "authorizationCode" in data:
        out["authorization_code"] = data["authorizationCode"]
    if "redirectUri" in data:
        out["redirect_uri"] = data["redirectUri"]
    return out