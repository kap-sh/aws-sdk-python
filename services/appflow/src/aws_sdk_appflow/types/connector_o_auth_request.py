"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorOAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.auth_code
    import aws_sdk_appflow.types.redirect_uri


class ConnectorOAuthRequest(TypedDict, closed=True):
    auth_code: NotRequired["aws_sdk_appflow.types.auth_code.AuthCode"]
    """<p> The code provided by the connector when it has been authenticated via the connected app. </p>"""
    redirect_uri: NotRequired["aws_sdk_appflow.types.redirect_uri.RedirectUri"]
    """<p> The URL to which the authentication server redirects the browser after authorization has been granted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOAuthRequest) -> dict:
    out: dict = {}
    if "auth_code" in value:
        out["authCode"] = value["auth_code"]
    if "redirect_uri" in value:
        out["redirectUri"] = value["redirect_uri"]
    return out


def deserialize_json(data: dict) -> ConnectorOAuthRequest:
    out: ConnectorOAuthRequest = {}  # type: ignore[typeddict-item]
    if "authCode" in data:
        out["auth_code"] = data["authCode"]
    if "redirectUri" in data:
        out["redirect_uri"] = data["redirectUri"]
    return out
