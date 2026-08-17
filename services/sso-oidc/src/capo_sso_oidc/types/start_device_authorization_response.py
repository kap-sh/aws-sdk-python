"""Generated from Smithy shape ``com.amazonaws.ssooidc#StartDeviceAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_oidc.types.device_code
    import capo_sso_oidc.types.expiration_in_seconds
    import capo_sso_oidc.types.interval_in_seconds
    import capo_sso_oidc.types.uri
    import capo_sso_oidc.types.user_code


class StartDeviceAuthorizationResponse(TypedDict, closed=True):
    device_code: NotRequired["capo_sso_oidc.types.device_code.DeviceCode"]
    """<p>The short-lived code that is used by the device when polling for a session token.</p>"""
    user_code: NotRequired["capo_sso_oidc.types.user_code.UserCode"]
    """<p>A one-time user verification code. This is needed to authorize an in-use device.</p>"""
    verification_uri: NotRequired["capo_sso_oidc.types.uri.URI"]
    """<p>The URI of the verification page that takes the <code>userCode</code> to authorize the device.</p>"""
    verification_uri_complete: NotRequired["capo_sso_oidc.types.uri.URI"]
    """<p>An alternate URL that the client can use to automatically launch a browser. This process skips the manual step in which the user visits the verification page and enters their code.</p>"""
    expires_in: "capo_sso_oidc.types.expiration_in_seconds.ExpirationInSeconds"
    """<p>Indicates the number of seconds in which the verification code will become invalid.</p>"""
    interval: "capo_sso_oidc.types.interval_in_seconds.IntervalInSeconds"
    """<p>Indicates the number of seconds the client must wait between attempts when polling for a session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeviceAuthorizationResponse) -> dict:
    out: dict = {}
    if "device_code" in value:
        out["deviceCode"] = value["device_code"]
    if "user_code" in value:
        out["userCode"] = value["user_code"]
    if "verification_uri" in value:
        out["verificationUri"] = value["verification_uri"]
    if "verification_uri_complete" in value:
        out["verificationUriComplete"] = value["verification_uri_complete"]
    out["expiresIn"] = value.get("expires_in", 0)
    out["interval"] = value.get("interval", 0)
    return out


def deserialize_json(data: dict) -> StartDeviceAuthorizationResponse:
    out: StartDeviceAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("deviceCode") is not None:
        out["device_code"] = data["deviceCode"]
    if data.get("userCode") is not None:
        out["user_code"] = data["userCode"]
    if data.get("verificationUri") is not None:
        out["verification_uri"] = data["verificationUri"]
    if data.get("verificationUriComplete") is not None:
        out["verification_uri_complete"] = data["verificationUriComplete"]
    if data.get("expiresIn") is not None:
        out["expires_in"] = data["expiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("interval") is not None:
        out["interval"] = data["interval"]
    else:
        out["interval"] = 0
    return out
