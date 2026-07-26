"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfTeletextPageType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.teletext_page_type

__listOfTeletextPageType: TypeAlias = list[
    "capo_mediaconvert.types.teletext_page_type.TeletextPageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTeletextPageType) -> list:
    import capo_mediaconvert.types.teletext_page_type

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.teletext_page_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTeletextPageType:
    import capo_mediaconvert.types.teletext_page_type

    out: __listOfTeletextPageType = []
    for item in data:
        out.append(capo_mediaconvert.types.teletext_page_type.deserialize_json(item))
    return out
