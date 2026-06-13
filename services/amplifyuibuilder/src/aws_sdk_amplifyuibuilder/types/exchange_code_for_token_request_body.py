"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExchangeCodeForTokenRequestBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.sensitive_string


class ExchangeCodeForTokenRequestBody(TypedDict):
    code: "aws_sdk_amplifyuibuilder.types.sensitive_string.SensitiveString"
    """<p>The access code to send in the request.</p>"""
    redirect_uri: "str"
    """<p>The location of the application that will receive the access code.</p>"""
    client_id: NotRequired[
        "aws_sdk_amplifyuibuilder.types.sensitive_string.SensitiveString"
    ]
    """<p>The ID of the client to request the token from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExchangeCodeForTokenRequestBody) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["redirectUri"] = value["redirect_uri"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> ExchangeCodeForTokenRequestBody:
    out: ExchangeCodeForTokenRequestBody = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ExchangeCodeForTokenRequestBody.code required")
    if "redirectUri" in data:
        out["redirect_uri"] = data["redirectUri"]
    else:
        raise DeserializationError(
            "ExchangeCodeForTokenRequestBody.redirect_uri required"
        )
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out
