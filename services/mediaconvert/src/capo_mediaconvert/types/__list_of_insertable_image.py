"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfInsertableImage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.insertable_image

__listOfInsertableImage: TypeAlias = list[
    "capo_mediaconvert.types.insertable_image.InsertableImage"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInsertableImage) -> list:
    import capo_mediaconvert.types.insertable_image

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.insertable_image.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInsertableImage:
    import capo_mediaconvert.types.insertable_image

    out: __listOfInsertableImage = []
    for item in data:
        out.append(capo_mediaconvert.types.insertable_image.deserialize_json(item))
    return out
