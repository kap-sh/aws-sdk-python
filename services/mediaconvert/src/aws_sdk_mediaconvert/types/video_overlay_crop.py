"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayCrop``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.video_overlay_unit


class VideoOverlayCrop(TypedDict, closed=True):
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the height of the video overlay cropping rectangle. To use the same height as your overlay input video: Keep blank, or enter 0. To specify a different height for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will be 100 pixels high. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 108 pixels high."""
    unit: NotRequired["aws_sdk_mediaconvert.types.video_overlay_unit.VideoOverlayUnit"]
    """Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the width of the video overlay cropping rectangle. To use the same width as your overlay input video: Keep blank, or enter 0. To specify a different width for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will be 100 pixels wide. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 192 pixels wide."""
    x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the distance between the cropping rectangle and the left edge of your overlay video's frame. To position the cropping rectangle along the left edge: Keep blank, or enter 0. To position the cropping rectangle to the right, relative to the left edge of your overlay video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the left edge of the overlay video's frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 192 pixels from the left edge of the overlay video's frame."""
    y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the distance between the cropping rectangle and the top edge of your overlay video's frame. To position the cropping rectangle along the top edge: Keep blank, or enter 0. To position the cropping rectangle down, relative to the top edge of your overlay video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the top edge of the overlay video's frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 108 pixels from the top edge of the overlay video's frame."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayCrop) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "unit" in value:
        import aws_sdk_mediaconvert.types.video_overlay_unit

        out["unit"] = aws_sdk_mediaconvert.types.video_overlay_unit.serialize_json(
            value["unit"]
        )
    if "width" in value:
        out["width"] = value["width"]
    if "x" in value:
        out["x"] = value["x"]
    if "y" in value:
        out["y"] = value["y"]
    return out


def deserialize_json(data: dict) -> VideoOverlayCrop:
    out: VideoOverlayCrop = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "unit" in data:
        import aws_sdk_mediaconvert.types.video_overlay_unit

        out["unit"] = aws_sdk_mediaconvert.types.video_overlay_unit.deserialize_json(
            data["unit"]
        )
    if "width" in data:
        out["width"] = data["width"]
    if "x" in data:
        out["x"] = data["x"]
    if "y" in data:
        out["y"] = data["y"]
    return out
