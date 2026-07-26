"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfMultiViewSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.multi_view_settings

__listOfMultiViewSettings: TypeAlias = list[
    "capo_mediaconvert.types.multi_view_settings.MultiViewSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiViewSettings) -> list:
    import capo_mediaconvert.types.multi_view_settings

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.multi_view_settings.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMultiViewSettings:
    import capo_mediaconvert.types.multi_view_settings

    out: __listOfMultiViewSettings = []
    for item in data:
        out.append(capo_mediaconvert.types.multi_view_settings.deserialize_json(item))
    return out
