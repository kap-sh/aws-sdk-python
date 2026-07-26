"""Generated from Smithy shape ``com.amazonaws.connect#MediaItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.media_source
    import capo_connect.types.media_type


class MediaItem(TypedDict, closed=True):
    type: NotRequired["capo_connect.types.media_type.MediaType"]
    """<p>The type of media. Valid values are: <code>IMAGE_LOGO_FAVICON</code> and <code>IMAGE_LOGO_HORIZONTAL</code>.</p>"""
    source: NotRequired["capo_connect.types.media_source.MediaSource"]
    """<p>The source URL or data for the media asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaItem) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connect.types.media_type

        out["Type"] = capo_connect.types.media_type.serialize_json(value["type"])
    if "source" in value:
        out["Source"] = value["source"]
    return out


def deserialize_json(data: dict) -> MediaItem:
    out: MediaItem = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.media_type

        out["type"] = capo_connect.types.media_type.deserialize_json(data["Type"])
    if "Source" in data:
        out["source"] = data["Source"]
    return out
