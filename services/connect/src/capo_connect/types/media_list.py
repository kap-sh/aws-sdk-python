"""Generated from Smithy shape ``com.amazonaws.connect#MediaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.media_item

MediaList: TypeAlias = list["capo_connect.types.media_item.MediaItem"]


# --- restJson1 ser/de ---
def serialize_json(value: MediaList) -> list:
    import capo_connect.types.media_item

    out: list = []
    for item in value:
        out.append(capo_connect.types.media_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MediaList:
    import capo_connect.types.media_item

    out: MediaList = []
    for item in data:
        out.append(capo_connect.types.media_item.deserialize_json(item))
    return out
