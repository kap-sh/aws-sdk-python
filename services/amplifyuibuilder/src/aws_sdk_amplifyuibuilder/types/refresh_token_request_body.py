"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RefreshTokenRequestBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.sensitive_string


class RefreshTokenRequestBody(TypedDict):
    token: "aws_sdk_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The token to use to refresh a previously issued access token that might have expired.</p>"""
    client_id: NotRequired[
        "aws_sdk_amplifyuibuilder.types.sensitive_string.SensitiveString"
    ]
    """<p>The ID of the client to request the token from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshTokenRequestBody) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> RefreshTokenRequestBody:
    out: RefreshTokenRequestBody = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("RefreshTokenRequestBody.token required")
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out
