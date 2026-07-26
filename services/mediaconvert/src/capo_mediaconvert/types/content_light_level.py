"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ContentLightLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer


class ContentLightLevel(TypedDict, closed=True):
    max_content_light_level: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Maximum content light level (MaxCLL), in cd/m²."""
    max_frame_average_light_level: NotRequired[
        "capo_mediaconvert.types.__integer.__integer"
    ]
    """Maximum frame-average light level (MaxFALL), in cd/m²."""


# --- restJson1 ser/de ---
def serialize_json(value: ContentLightLevel) -> dict:
    out: dict = {}
    if "max_content_light_level" in value:
        out["maxContentLightLevel"] = value["max_content_light_level"]
    if "max_frame_average_light_level" in value:
        out["maxFrameAverageLightLevel"] = value["max_frame_average_light_level"]
    return out


def deserialize_json(data: dict) -> ContentLightLevel:
    out: ContentLightLevel = {}  # type: ignore[typeddict-item]
    if "maxContentLightLevel" in data:
        out["max_content_light_level"] = data["maxContentLightLevel"]
    if "maxFrameAverageLightLevel" in data:
        out["max_frame_average_light_level"] = data["maxFrameAverageLightLevel"]
    return out
