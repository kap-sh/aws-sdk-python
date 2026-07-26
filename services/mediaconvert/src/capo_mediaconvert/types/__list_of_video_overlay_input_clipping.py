"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfVideoOverlayInputClipping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.video_overlay_input_clipping

__listOfVideoOverlayInputClipping: TypeAlias = list[
    "capo_mediaconvert.types.video_overlay_input_clipping.VideoOverlayInputClipping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoOverlayInputClipping) -> list:
    import capo_mediaconvert.types.video_overlay_input_clipping

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.video_overlay_input_clipping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfVideoOverlayInputClipping:
    import capo_mediaconvert.types.video_overlay_input_clipping

    out: __listOfVideoOverlayInputClipping = []
    for item in data:
        out.append(
            capo_mediaconvert.types.video_overlay_input_clipping.deserialize_json(item)
        )
    return out
