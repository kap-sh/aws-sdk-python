"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfThumbnail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.thumbnail

__listOfThumbnail: TypeAlias = list["capo_medialive.types.thumbnail.Thumbnail"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfThumbnail) -> list:
    import capo_medialive.types.thumbnail

    out: list = []
    for item in value:
        out.append(capo_medialive.types.thumbnail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfThumbnail:
    import capo_medialive.types.thumbnail

    out: __listOfThumbnail = []
    for item in data:
        out.append(capo_medialive.types.thumbnail.deserialize_json(item))
    return out
