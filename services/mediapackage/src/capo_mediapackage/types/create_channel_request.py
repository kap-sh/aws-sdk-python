"""Generated from Smithy shape ``com.amazonaws.mediapackage#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.tags


class CreateChannelRequest(TypedDict, closed=True):
    description: NotRequired["capo_mediapackage.types.__string.__string"]
    """A short text description of the Channel."""
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the Channel. The ID must be unique within the region and it cannot be changed after a Channel is created."""
    tags: NotRequired["capo_mediapackage.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import capo_mediapackage.types.tags

        out["tags"] = capo_mediapackage.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "tags" in data:
        import capo_mediapackage.types.tags

        out["tags"] = capo_mediapackage.types.tags.deserialize_json(data["tags"])
    return out
