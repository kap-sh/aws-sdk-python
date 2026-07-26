"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExchangeCodeForTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sensitive_string


class ExchangeCodeForTokenResponse(TypedDict, closed=True):
    access_token: "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The access token.</p>"""
    expires_in: "int"
    """<p>The date and time when the new access token expires.</p>"""
    refresh_token: "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The token to use to refresh a previously issued access token that might have expired.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExchangeCodeForTokenResponse) -> dict:
    out: dict = {}
    out["accessToken"] = value["access_token"]
    out["expiresIn"] = value["expires_in"]
    out["refreshToken"] = value["refresh_token"]
    return out


def deserialize_json(data: dict) -> ExchangeCodeForTokenResponse:
    out: ExchangeCodeForTokenResponse = {}  # type: ignore[typeddict-item]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    else:
        raise DeserializationError("ExchangeCodeForTokenResponse.access_token required")
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    else:
        raise DeserializationError("ExchangeCodeForTokenResponse.expires_in required")
    if "refreshToken" in data:
        out["refresh_token"] = data["refreshToken"]
    else:
        raise DeserializationError(
            "ExchangeCodeForTokenResponse.refresh_token required"
        )
    return out
