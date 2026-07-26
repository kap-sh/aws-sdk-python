"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RefreshTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sensitive_string


class RefreshTokenResponse(TypedDict, closed=True):
    access_token: "capo_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The access token.</p>"""
    expires_in: "int"
    """<p>The date and time when the new access token expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshTokenResponse) -> dict:
    out: dict = {}
    out["accessToken"] = value["access_token"]
    out["expiresIn"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> RefreshTokenResponse:
    out: RefreshTokenResponse = {}  # type: ignore[typeddict-item]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    else:
        raise DeserializationError("RefreshTokenResponse.access_token required")
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    else:
        raise DeserializationError("RefreshTokenResponse.expires_in required")
    return out
