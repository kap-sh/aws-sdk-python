"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputVideoGenerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max32
    import capo_mediaconvert.types.__integer_min1_max1001
    import capo_mediaconvert.types.__integer_min1_max60000
    import capo_mediaconvert.types.__integer_min1_max86400000
    import capo_mediaconvert.types.__integer_min32_max8192
    import capo_mediaconvert.types.__integer_min32000_max48000
    import capo_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_tga_tga_https_bmp_bmp_png_png_tga_tga


class InputVideoGenerator(TypedDict, closed=True):
    channels: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max32.__integerMin1Max32"
    ]
    """Specify the number of audio channels to include in your video generator input. MediaConvert creates these audio channels as silent audio within a single audio track. Enter an integer from 1 to 32."""
    duration: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max86400000.__integerMin1Max86400000"
    ]
    """Specify the duration, in milliseconds, for your video generator input. Enter an integer from 1 to 86400000."""
    framerate_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max1001.__integerMin1Max1001"
    ]
    """Specify the denominator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate numerator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank."""
    framerate_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max60000.__integerMin1Max60000"
    ]
    """Specify the numerator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate denominator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank."""
    height: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Specify the height, in pixels, for your video generator input. This is useful for positioning when you include one or more video overlays for this input. To use the default resolution 540x360: Leave both width and height blank. To specify a height: Enter an even integer from 32 to 8192. When you do, you must also specify a value for width."""
    image_input: NotRequired[
        "capo_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_tga_tga_https_bmp_bmp_png_png_tga_tga.__stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA"
    ]
    """Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min32000_max48000.__integerMin32000Max48000"
    ]
    """Specify the audio sample rate, in Hz, for the silent audio in your video generator input. Enter an integer from 32000 to 48000."""
    width: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Specify the width, in pixels, for your video generator input. This is useful for positioning when you include one or more video overlays for this input. To use the default resolution 540x360: Leave both width and height blank. To specify a width: Enter an even integer from 32 to 8192. When you do, you must also specify a value for height."""


# --- restJson1 ser/de ---
def serialize_json(value: InputVideoGenerator) -> dict:
    out: dict = {}
    if "channels" in value:
        out["channels"] = value["channels"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "height" in value:
        out["height"] = value["height"]
    if "image_input" in value:
        out["imageInput"] = value["image_input"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> InputVideoGenerator:
    out: InputVideoGenerator = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "height" in data:
        out["height"] = data["height"]
    if "imageInput" in data:
        out["image_input"] = data["imageInput"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "width" in data:
        out["width"] = data["width"]
    return out
