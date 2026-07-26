"""Generated from Smithy shape ``com.amazonaws.medialive#AudioHlsRenditionSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1


class AudioHlsRenditionSelection(TypedDict, closed=True):
    group_id: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """Specifies the GROUP-ID in the #EXT-X-MEDIA tag of the target HLS audio rendition."""
    name: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """Specifies the NAME in the #EXT-X-MEDIA tag of the target HLS audio rendition."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioHlsRenditionSelection) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AudioHlsRenditionSelection:
    out: AudioHlsRenditionSelection = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "name" in data:
        out["name"] = data["name"]
    return out
