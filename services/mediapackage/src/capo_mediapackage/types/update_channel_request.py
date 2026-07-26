"""Generated from Smithy shape ``com.amazonaws.mediapackage#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string


class UpdateChannelRequest(TypedDict, closed=True):
    description: NotRequired["capo_mediapackage.types.__string.__string"]
    """A short text description of the Channel."""
    id: "capo_mediapackage.types.__string.__string"
    """The ID of the Channel to update."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
