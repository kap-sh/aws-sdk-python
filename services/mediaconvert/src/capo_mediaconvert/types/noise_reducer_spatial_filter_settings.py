"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducerSpatialFilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max3
    import capo_mediaconvert.types.__integer_min0_max16
    import capo_mediaconvert.types.__integer_min_negative2_max3


class NoiseReducerSpatialFilterSettings(TypedDict, closed=True):
    post_filter_sharpen_strength: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max3.__integerMin0Max3"
    ]
    """Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength."""
    speed: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative2_max3.__integerMinNegative2Max3"
    ]
    """The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value."""
    strength: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max16.__integerMin0Max16"
    ]
    """Relative strength of noise reducing filter. Higher values produce stronger filtering."""


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducerSpatialFilterSettings) -> dict:
    out: dict = {}
    if "post_filter_sharpen_strength" in value:
        out["postFilterSharpenStrength"] = value["post_filter_sharpen_strength"]
    if "speed" in value:
        out["speed"] = value["speed"]
    if "strength" in value:
        out["strength"] = value["strength"]
    return out


def deserialize_json(data: dict) -> NoiseReducerSpatialFilterSettings:
    out: NoiseReducerSpatialFilterSettings = {}  # type: ignore[typeddict-item]
    if "postFilterSharpenStrength" in data:
        out["post_filter_sharpen_strength"] = data["postFilterSharpenStrength"]
    if "speed" in data:
        out["speed"] = data["speed"]
    if "strength" in data:
        out["strength"] = data["strength"]
    return out
