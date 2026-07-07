"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessagingSessionEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.url_type


class MessagingSessionEndpoint(TypedDict, closed=True):
    url: NotRequired["aws_sdk_chime_sdk_messaging.types.url_type.UrlType"]
    """<p>The endpoint to which you establish a websocket connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessagingSessionEndpoint) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> MessagingSessionEndpoint:
    out: MessagingSessionEndpoint = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
