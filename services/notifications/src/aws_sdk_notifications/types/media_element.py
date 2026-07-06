"""Generated from Smithy shape ``com.amazonaws.notifications#MediaElement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.media_element_type
    import aws_sdk_notifications.types.media_id
    import aws_sdk_notifications.types.text_part_reference
    import aws_sdk_notifications.types.url


class MediaElement(TypedDict, closed=True):
    media_id: "aws_sdk_notifications.types.media_id.MediaId"
    """<p>The unique ID for the media.</p>"""
    type: "aws_sdk_notifications.types.media_element_type.MediaElementType"
    """<p>The type of media.</p>"""
    url: "aws_sdk_notifications.types.url.Url"
    """<p>The URL of the media.</p>"""
    caption: "aws_sdk_notifications.types.text_part_reference.TextPartReference"
    """<p>The caption of the media.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaElement) -> dict:
    out: dict = {}
    out["mediaId"] = value["media_id"]
    out["type"] = value["type"]
    out["url"] = value["url"]
    out["caption"] = value["caption"]
    return out


def deserialize_json(data: dict) -> MediaElement:
    out: MediaElement = {}  # type: ignore[typeddict-item]
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    else:
        raise DeserializationError("MediaElement.media_id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("MediaElement.type required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("MediaElement.url required")
    if "caption" in data:
        out["caption"] = data["caption"]
    else:
        raise DeserializationError("MediaElement.caption required")
    return out
