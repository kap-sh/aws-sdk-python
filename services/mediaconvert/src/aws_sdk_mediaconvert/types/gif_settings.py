"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GifSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.gif_framerate_control
    import aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm


class GifSettings(TypedDict):
    framerate_control: NotRequired[
        "aws_sdk_mediaconvert.types.gif_framerate_control.GifFramerateControl"
    ]
    """If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator."""
    framerate_conversion_algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm.GifFramerateConversionAlgorithm"
    ]
    """Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion."""
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""


# --- restJson1 ser/de ---
def serialize_json(value: GifSettings) -> dict:
    out: dict = {}
    if "framerate_control" in value:
        import aws_sdk_mediaconvert.types.gif_framerate_control

        out["framerateControl"] = (
            aws_sdk_mediaconvert.types.gif_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    return out


def deserialize_json(data: dict) -> GifSettings:
    out: GifSettings = {}  # type: ignore[typeddict-item]
    if "framerateControl" in data:
        import aws_sdk_mediaconvert.types.gif_framerate_control

        out["framerate_control"] = (
            aws_sdk_mediaconvert.types.gif_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            aws_sdk_mediaconvert.types.gif_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    return out
