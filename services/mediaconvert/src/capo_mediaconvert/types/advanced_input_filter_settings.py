"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AdvancedInputFilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.advanced_input_filter_add_texture
    import capo_mediaconvert.types.advanced_input_filter_sharpen


class AdvancedInputFilterSettings(TypedDict, closed=True):
    add_texture: NotRequired[
        "capo_mediaconvert.types.advanced_input_filter_add_texture.AdvancedInputFilterAddTexture"
    ]
    """Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesn't have texture, including screen recordings, computer graphics, or cartoons."""
    sharpening: NotRequired[
        "capo_mediaconvert.types.advanced_input_filter_sharpen.AdvancedInputFilterSharpen"
    ]
    """Optionally specify the amount of sharpening to apply when you use the Advanced input filter. Sharpening adds contrast to the edges of your video content and can reduce softness. To apply no sharpening: Keep the default value, Off. To apply a minimal amount of sharpening choose Low, or for the maximum choose High."""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedInputFilterSettings) -> dict:
    out: dict = {}
    if "add_texture" in value:
        import capo_mediaconvert.types.advanced_input_filter_add_texture

        out["addTexture"] = (
            capo_mediaconvert.types.advanced_input_filter_add_texture.serialize_json(
                value["add_texture"]
            )
        )
    if "sharpening" in value:
        import capo_mediaconvert.types.advanced_input_filter_sharpen

        out["sharpening"] = (
            capo_mediaconvert.types.advanced_input_filter_sharpen.serialize_json(
                value["sharpening"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdvancedInputFilterSettings:
    out: AdvancedInputFilterSettings = {}  # type: ignore[typeddict-item]
    if "addTexture" in data:
        import capo_mediaconvert.types.advanced_input_filter_add_texture

        out["add_texture"] = (
            capo_mediaconvert.types.advanced_input_filter_add_texture.deserialize_json(
                data["addTexture"]
            )
        )
    if "sharpening" in data:
        import capo_mediaconvert.types.advanced_input_filter_sharpen

        out["sharpening"] = (
            capo_mediaconvert.types.advanced_input_filter_sharpen.deserialize_json(
                data["sharpening"]
            )
        )
    return out
