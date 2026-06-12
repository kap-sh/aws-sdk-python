"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InsertableImage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max99
    import aws_sdk_mediaconvert.types.__integer_min0_max100
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_tga_tga_https_bmp_bmp_png_png_tga_tga
    import aws_sdk_mediaconvert.types.__string_pattern01_d20305_d205_d


class InsertableImage(TypedDict):
    duration: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the time, in milliseconds, for the image to remain on the output video. This duration includes fade-in time but not fade-out time."""
    fade_in: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the length of time, in milliseconds, between the Start time that you specify for the image insertion and the time that the image appears at full opacity. Full opacity is the level that you specify for the opacity setting. If you don't specify a value for Fade-in, the image will appear abruptly at the overlay start time."""
    fade_out: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the length of time, in milliseconds, between the end of the time that you have specified for the image overlay Duration and when the overlaid image has faded to total transparency. If you don't specify a value for Fade-out, the image will disappear abruptly at the end of the inserted image duration."""
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the height of the inserted image in pixels. If you specify a value that's larger than the video resolution height, the service will crop your overlaid image to fit. To use the native height of the image, keep this setting blank."""
    image_inserter_input: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_tga_tga_https_bmp_bmp_png_png_tga_tga.__stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA"
    ]
    """Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file."""
    image_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the distance, in pixels, between the inserted image and the left edge of the video frame. Required for any image overlay that you specify."""
    image_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the distance, in pixels, between the overlaid image and the top edge of the video frame. Required for any image overlay that you specify."""
    layer: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max99.__integerMin0Max99"
    ]
    """Specify how overlapping inserted images appear. Images with higher values for Layer appear on top of images with lower values for Layer."""
    opacity: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Use Opacity to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50."""
    start_time: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern01_d20305_d205_d.__stringPattern01D20305D205D"
    ]
    """Specify the timecode of the frame that you want the overlay to first appear on. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your timecode source settings."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the width of the inserted image in pixels. If you specify a value that's larger than the video resolution width, the service will crop your overlaid image to fit. To use the native width of the image, keep this setting blank."""


# --- restJson1 ser/de ---
def serialize_json(value: InsertableImage) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "fade_in" in value:
        out["fadeIn"] = value["fade_in"]
    if "fade_out" in value:
        out["fadeOut"] = value["fade_out"]
    if "height" in value:
        out["height"] = value["height"]
    if "image_inserter_input" in value:
        out["imageInserterInput"] = value["image_inserter_input"]
    if "image_x" in value:
        out["imageX"] = value["image_x"]
    if "image_y" in value:
        out["imageY"] = value["image_y"]
    if "layer" in value:
        out["layer"] = value["layer"]
    if "opacity" in value:
        out["opacity"] = value["opacity"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> InsertableImage:
    out: InsertableImage = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "fadeIn" in data:
        out["fade_in"] = data["fadeIn"]
    if "fadeOut" in data:
        out["fade_out"] = data["fadeOut"]
    if "height" in data:
        out["height"] = data["height"]
    if "imageInserterInput" in data:
        out["image_inserter_input"] = data["imageInserterInput"]
    if "imageX" in data:
        out["image_x"] = data["imageX"]
    if "imageY" in data:
        out["image_y"] = data["imageY"]
    if "layer" in data:
        out["layer"] = data["layer"]
    if "opacity" in data:
        out["opacity"] = data["opacity"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "width" in data:
        out["width"] = data["width"]
    return out
