"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.video_selector_color_space
    import capo_medialive.types.video_selector_color_space_settings
    import capo_medialive.types.video_selector_color_space_usage
    import capo_medialive.types.video_selector_settings


class VideoSelector(TypedDict, closed=True):
    color_space: NotRequired[
        "capo_medialive.types.video_selector_color_space.VideoSelectorColorSpace"
    ]
    """Controls how MediaLive will use the color space metadata from the source. Typically, choose FOLLOW, which means to use the color space metadata without changing it. Or choose another value (a standard). In this case, the handling is controlled by the colorspaceUsage property."""
    color_space_settings: NotRequired[
        "capo_medialive.types.video_selector_color_space_settings.VideoSelectorColorSpaceSettings"
    ]
    """Choose HDR10 only if the following situation applies. Firstly, you specified HDR10 in ColorSpace. Secondly, the attached input is for AWS Elemental Link. Thirdly, you plan to convert the content to another color space. You need to specify the color space metadata that is missing from the source sent from AWS Elemental Link."""
    color_space_usage: NotRequired[
        "capo_medialive.types.video_selector_color_space_usage.VideoSelectorColorSpaceUsage"
    ]
    """Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data."""
    selector_settings: NotRequired[
        "capo_medialive.types.video_selector_settings.VideoSelectorSettings"
    ]
    """The video selector settings."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelector) -> dict:
    out: dict = {}
    if "color_space" in value:
        import capo_medialive.types.video_selector_color_space

        out["colorSpace"] = (
            capo_medialive.types.video_selector_color_space.serialize_json(
                value["color_space"]
            )
        )
    if "color_space_settings" in value:
        import capo_medialive.types.video_selector_color_space_settings

        out["colorSpaceSettings"] = (
            capo_medialive.types.video_selector_color_space_settings.serialize_json(
                value["color_space_settings"]
            )
        )
    if "color_space_usage" in value:
        import capo_medialive.types.video_selector_color_space_usage

        out["colorSpaceUsage"] = (
            capo_medialive.types.video_selector_color_space_usage.serialize_json(
                value["color_space_usage"]
            )
        )
    if "selector_settings" in value:
        import capo_medialive.types.video_selector_settings

        out["selectorSettings"] = (
            capo_medialive.types.video_selector_settings.serialize_json(
                value["selector_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoSelector:
    out: VideoSelector = {}  # type: ignore[typeddict-item]
    if "colorSpace" in data:
        import capo_medialive.types.video_selector_color_space

        out["color_space"] = (
            capo_medialive.types.video_selector_color_space.deserialize_json(
                data["colorSpace"]
            )
        )
    if "colorSpaceSettings" in data:
        import capo_medialive.types.video_selector_color_space_settings

        out["color_space_settings"] = (
            capo_medialive.types.video_selector_color_space_settings.deserialize_json(
                data["colorSpaceSettings"]
            )
        )
    if "colorSpaceUsage" in data:
        import capo_medialive.types.video_selector_color_space_usage

        out["color_space_usage"] = (
            capo_medialive.types.video_selector_color_space_usage.deserialize_json(
                data["colorSpaceUsage"]
            )
        )
    if "selectorSettings" in data:
        import capo_medialive.types.video_selector_settings

        out["selector_settings"] = (
            capo_medialive.types.video_selector_settings.deserialize_json(
                data["selectorSettings"]
            )
        )
    return out
