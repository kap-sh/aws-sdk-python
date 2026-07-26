"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vc3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max1001
    import capo_mediaconvert.types.__integer_min24_max60000
    import capo_mediaconvert.types.vc3_class
    import capo_mediaconvert.types.vc3_framerate_control
    import capo_mediaconvert.types.vc3_framerate_conversion_algorithm
    import capo_mediaconvert.types.vc3_interlace_mode
    import capo_mediaconvert.types.vc3_scan_type_conversion_mode
    import capo_mediaconvert.types.vc3_slow_pal
    import capo_mediaconvert.types.vc3_telecine


class Vc3Settings(TypedDict, closed=True):
    framerate_control: NotRequired[
        "capo_mediaconvert.types.vc3_framerate_control.Vc3FramerateControl"
    ]
    """If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "capo_mediaconvert.types.vc3_framerate_conversion_algorithm.Vc3FramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max1001.__integerMin1Max1001"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min24_max60000.__integerMin24Max60000"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    interlace_mode: NotRequired[
        "capo_mediaconvert.types.vc3_interlace_mode.Vc3InterlaceMode"
    ]
    """Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output."""
    scan_type_conversion_mode: NotRequired[
        "capo_mediaconvert.types.vc3_scan_type_conversion_mode.Vc3ScanTypeConversionMode"
    ]
    """Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive."""
    slow_pal: NotRequired["capo_mediaconvert.types.vc3_slow_pal.Vc3SlowPal"]
    """Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25."""
    telecine: NotRequired["capo_mediaconvert.types.vc3_telecine.Vc3Telecine"]
    """When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""
    vc3_class: NotRequired["capo_mediaconvert.types.vc3_class.Vc3Class"]
    """Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output."""


# --- restJson1 ser/de ---
def serialize_json(value: Vc3Settings) -> dict:
    out: dict = {}
    if "framerate_control" in value:
        import capo_mediaconvert.types.vc3_framerate_control

        out["framerateControl"] = (
            capo_mediaconvert.types.vc3_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import capo_mediaconvert.types.vc3_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            capo_mediaconvert.types.vc3_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "interlace_mode" in value:
        import capo_mediaconvert.types.vc3_interlace_mode

        out["interlaceMode"] = (
            capo_mediaconvert.types.vc3_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "scan_type_conversion_mode" in value:
        import capo_mediaconvert.types.vc3_scan_type_conversion_mode

        out["scanTypeConversionMode"] = (
            capo_mediaconvert.types.vc3_scan_type_conversion_mode.serialize_json(
                value["scan_type_conversion_mode"]
            )
        )
    if "slow_pal" in value:
        import capo_mediaconvert.types.vc3_slow_pal

        out["slowPal"] = capo_mediaconvert.types.vc3_slow_pal.serialize_json(
            value["slow_pal"]
        )
    if "telecine" in value:
        import capo_mediaconvert.types.vc3_telecine

        out["telecine"] = capo_mediaconvert.types.vc3_telecine.serialize_json(
            value["telecine"]
        )
    if "vc3_class" in value:
        import capo_mediaconvert.types.vc3_class

        out["vc3Class"] = capo_mediaconvert.types.vc3_class.serialize_json(
            value["vc3_class"]
        )
    return out


def deserialize_json(data: dict) -> Vc3Settings:
    out: Vc3Settings = {}  # type: ignore[typeddict-item]
    if "framerateControl" in data:
        import capo_mediaconvert.types.vc3_framerate_control

        out["framerate_control"] = (
            capo_mediaconvert.types.vc3_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import capo_mediaconvert.types.vc3_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            capo_mediaconvert.types.vc3_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "interlaceMode" in data:
        import capo_mediaconvert.types.vc3_interlace_mode

        out["interlace_mode"] = (
            capo_mediaconvert.types.vc3_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if "scanTypeConversionMode" in data:
        import capo_mediaconvert.types.vc3_scan_type_conversion_mode

        out["scan_type_conversion_mode"] = (
            capo_mediaconvert.types.vc3_scan_type_conversion_mode.deserialize_json(
                data["scanTypeConversionMode"]
            )
        )
    if "slowPal" in data:
        import capo_mediaconvert.types.vc3_slow_pal

        out["slow_pal"] = capo_mediaconvert.types.vc3_slow_pal.deserialize_json(
            data["slowPal"]
        )
    if "telecine" in data:
        import capo_mediaconvert.types.vc3_telecine

        out["telecine"] = capo_mediaconvert.types.vc3_telecine.deserialize_json(
            data["telecine"]
        )
    if "vc3Class" in data:
        import capo_mediaconvert.types.vc3_class

        out["vc3_class"] = capo_mediaconvert.types.vc3_class.deserialize_json(
            data["vc3Class"]
        )
    return out
