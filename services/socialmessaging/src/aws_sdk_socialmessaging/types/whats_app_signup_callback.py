"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppSignupCallback``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError


class WhatsAppSignupCallback(TypedDict, closed=True):
    access_token: "str"
    """<p>The access token for your WhatsApp Business Account. The <code>accessToken</code> value is provided by Meta.</p>"""
    callback_url: NotRequired["str"]
    """<p>The URL where WhatsApp will send callback notifications for this account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppSignupCallback) -> dict:
    out: dict = {}
    out["accessToken"] = value["access_token"]
    if "callback_url" in value:
        out["callbackUrl"] = value["callback_url"]
    return out


def deserialize_json(data: dict) -> WhatsAppSignupCallback:
    out: WhatsAppSignupCallback = {}  # type: ignore[typeddict-item]
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    else:
        raise DeserializationError("WhatsAppSignupCallback.access_token required")
    if "callbackUrl" in data:
        out["callback_url"] = data["callbackUrl"]
    return out
