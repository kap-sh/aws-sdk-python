"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HdrMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.content_light_level
    import capo_mediaconvert.types.mastering_display_color_volume


class HdrMetadata(TypedDict, closed=True):
    content_light_level: NotRequired[
        "capo_mediaconvert.types.content_light_level.ContentLightLevel"
    ]
    """Content light level information (CTA-861.3). Describes the light level characteristics of the content."""
    mastering_display_color_volume: NotRequired[
        "capo_mediaconvert.types.mastering_display_color_volume.MasteringDisplayColorVolume"
    ]
    """Mastering display color volume metadata (SMPTE ST 2086). Describes the color volume of the display used to master the content. Chromaticity coordinates are in units of 0.00002. Luminance values are in units of 0.0001 cd/m²."""


# --- restJson1 ser/de ---
def serialize_json(value: HdrMetadata) -> dict:
    out: dict = {}
    if "content_light_level" in value:
        import capo_mediaconvert.types.content_light_level

        out["contentLightLevel"] = (
            capo_mediaconvert.types.content_light_level.serialize_json(
                value["content_light_level"]
            )
        )
    if "mastering_display_color_volume" in value:
        import capo_mediaconvert.types.mastering_display_color_volume

        out["masteringDisplayColorVolume"] = (
            capo_mediaconvert.types.mastering_display_color_volume.serialize_json(
                value["mastering_display_color_volume"]
            )
        )
    return out


def deserialize_json(data: dict) -> HdrMetadata:
    out: HdrMetadata = {}  # type: ignore[typeddict-item]
    if "contentLightLevel" in data:
        import capo_mediaconvert.types.content_light_level

        out["content_light_level"] = (
            capo_mediaconvert.types.content_light_level.deserialize_json(
                data["contentLightLevel"]
            )
        )
    if "masteringDisplayColorVolume" in data:
        import capo_mediaconvert.types.mastering_display_color_volume

        out["mastering_display_color_volume"] = (
            capo_mediaconvert.types.mastering_display_color_volume.deserialize_json(
                data["masteringDisplayColorVolume"]
            )
        )
    return out
