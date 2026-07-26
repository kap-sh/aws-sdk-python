"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfThumbnailDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.thumbnail_detail

__listOfThumbnailDetail: TypeAlias = list[
    "capo_medialive.types.thumbnail_detail.ThumbnailDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfThumbnailDetail) -> list:
    import capo_medialive.types.thumbnail_detail

    out: list = []
    for item in value:
        out.append(capo_medialive.types.thumbnail_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfThumbnailDetail:
    import capo_medialive.types.thumbnail_detail

    out: __listOfThumbnailDetail = []
    for item in data:
        out.append(capo_medialive.types.thumbnail_detail.deserialize_json(item))
    return out
