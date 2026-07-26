"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AutomatedEncodingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.automated_abr_settings


class AutomatedEncodingSettings(TypedDict, closed=True):
    abr_settings: NotRequired[
        "capo_mediaconvert.types.automated_abr_settings.AutomatedAbrSettings"
    ]
    """Use automated ABR to have MediaConvert set up the renditions in your ABR package for you automatically, based on characteristics of your input video. This feature optimizes video quality while minimizing the overall size of your ABR package."""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEncodingSettings) -> dict:
    out: dict = {}
    if "abr_settings" in value:
        import capo_mediaconvert.types.automated_abr_settings

        out["abrSettings"] = (
            capo_mediaconvert.types.automated_abr_settings.serialize_json(
                value["abr_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedEncodingSettings:
    out: AutomatedEncodingSettings = {}  # type: ignore[typeddict-item]
    if "abrSettings" in data:
        import capo_mediaconvert.types.automated_abr_settings

        out["abr_settings"] = (
            capo_mediaconvert.types.automated_abr_settings.deserialize_json(
                data["abrSettings"]
            )
        )
    return out
