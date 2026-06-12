"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayPosition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max100
    import aws_sdk_mediaconvert.types.__integer_min_negative1_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import aws_sdk_mediaconvert.types.video_overlay_unit


class VideoOverlayPosition(TypedDict):
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative1_max2147483647.__integerMinNegative1Max2147483647"
    ]
    """To scale your video overlay to the same height as the base input video: Leave blank. To scale the height of your video overlay to a different height: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 360 and choose Pixels, your video overlay will be rendered with a height of 360. When you enter 50, choose Percentage, and your overlay's source has a height of 1080, your video overlay will be rendered with a height of 540. To scale your overlay to a specific height while automatically maintaining its original aspect ratio, enter a value for Height and leave Width blank."""
    opacity: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Use Opacity to specify how much of the underlying video shows through the overlay video. 0 is transparent and 100 is fully opaque. Default is 100."""
    unit: NotRequired["aws_sdk_mediaconvert.types.video_overlay_unit.VideoOverlayUnit"]
    """Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative1_max2147483647.__integerMinNegative1Max2147483647"
    ]
    """To scale your video overlay to the same width as the base input video: Leave blank. To scale the width of your video overlay to a different width: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 640 and choose Pixels, your video overlay will scale to a height of 640 pixels. When you enter 50, choose Percentage, and your overlay's source has a width of 1920, your video overlay will scale to a width of 960. To scale your overlay to a specific width while automatically maintaining its original aspect ratio, enter a value for Width and leave Height blank."""
    x_position: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """To position the left edge of your video overlay along the left edge of the base input video's frame: Keep blank, or enter 0. To position the left edge of your video overlay to the right, relative to the left edge of the base input video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the left edge of the base input video's frame. When you enter 10, choose Percentage, and your base input video is 1920x1080, your video overlay will be positioned 192 pixels from the left edge of the base input video's frame."""
    y_position: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """To position the top edge of your video overlay along the top edge of the base input video's frame: Keep blank, or enter 0. To position the top edge of your video overlay down, relative to the top edge of the base input video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the top edge of the base input video's frame. When you enter 10, choose Percentage, and your underlying video is 1920x1080, your video overlay will be positioned 108 pixels from the top edge of the base input video's frame."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayPosition) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "opacity" in value:
        out["opacity"] = value["opacity"]
    if "unit" in value:
        import aws_sdk_mediaconvert.types.video_overlay_unit

        out["unit"] = aws_sdk_mediaconvert.types.video_overlay_unit.serialize_json(
            value["unit"]
        )
    if "width" in value:
        out["width"] = value["width"]
    if "x_position" in value:
        out["xPosition"] = value["x_position"]
    if "y_position" in value:
        out["yPosition"] = value["y_position"]
    return out


def deserialize_json(data: dict) -> VideoOverlayPosition:
    out: VideoOverlayPosition = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "opacity" in data:
        out["opacity"] = data["opacity"]
    if "unit" in data:
        import aws_sdk_mediaconvert.types.video_overlay_unit

        out["unit"] = aws_sdk_mediaconvert.types.video_overlay_unit.deserialize_json(
            data["unit"]
        )
    if "width" in data:
        out["width"] = data["width"]
    if "xPosition" in data:
        out["x_position"] = data["xPosition"]
    if "yPosition" in data:
        out["y_position"] = data["yPosition"]
    return out
