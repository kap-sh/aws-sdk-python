"""Generated from Smithy shape ``com.amazonaws.datazone#GlueOAuth2Credentials``."""

from typing import TypedDict
from typing_extensions import NotRequired


class GlueOAuth2Credentials(TypedDict):
    user_managed_client_application_client_secret: NotRequired["str"]
    """<p>The user managed client application client secret of the connection. </p>"""
    access_token: NotRequired["str"]
    """<p>The access token of a connection.</p>"""
    refresh_token: NotRequired["str"]
    """<p>The refresh token of the connection.</p>"""
    jwt_token: NotRequired["str"]
    """<p>The jwt token of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueOAuth2Credentials) -> dict:
    out: dict = {}
    if "user_managed_client_application_client_secret" in value:
        out["userManagedClientApplicationClientSecret"] = value[
            "user_managed_client_application_client_secret"
        ]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "jwt_token" in value:
        out["jwtToken"] = value["jwt_token"]
    return out


def deserialize_json(data: dict) -> GlueOAuth2Credentials:
    out: GlueOAuth2Credentials = {}  # type: ignore[typeddict-item]
    if "userManagedClientApplicationClientSecret" in data:
        out["user_managed_client_application_client_secret"] = data[
            "userManagedClientApplicationClientSecret"
        ]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    if "jwtToken" in data:
        out["jwt_token"] = data["jwtToken"]
    return out
