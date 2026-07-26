"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string


class SMSChannelRequest(TypedDict, closed=True):
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the SMS channel for the application.</p>"""
    sender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The identity that you want to display on recipients' devices when they receive messages from the SMS channel.</p>"""
    short_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The registered short code that you want to use when you send messages through the SMS channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSChannelRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "short_code" in value:
        out["ShortCode"] = value["short_code"]
    return out


def deserialize_json(data: dict) -> SMSChannelRequest:
    out: SMSChannelRequest = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    if "ShortCode" in data:
        out["short_code"] = data["ShortCode"]
    return out
