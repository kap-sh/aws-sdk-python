"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0
    import capo_mediaconvert.types.__integer_min0_max47185920
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__integer_min1000_max480000000
    import capo_mediaconvert.types.vp9_framerate_control
    import capo_mediaconvert.types.vp9_framerate_conversion_algorithm
    import capo_mediaconvert.types.vp9_par_control
    import capo_mediaconvert.types.vp9_quality_tuning_level
    import capo_mediaconvert.types.vp9_rate_control_mode


class Vp9Settings(TypedDict, closed=True):
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max480000000.__integerMin1000Max480000000"
    ]
    """Target bitrate in bits/second. For example, enter five megabits per second as 5000000."""
    framerate_control: NotRequired[
        "capo_mediaconvert.types.vp9_framerate_control.Vp9FramerateControl"
    ]
    """If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "capo_mediaconvert.types.vp9_framerate_conversion_algorithm.Vp9FramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    gop_size: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """GOP Length (keyframe interval) in frames. Must be greater than zero."""
    hrd_buffer_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max47185920.__integerMin0Max47185920"
    ]
    """Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000."""
    max_bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max480000000.__integerMin1000Max480000000"
    ]
    """Ignore this setting unless you set qualityTuningLevel to MULTI_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate."""
    par_control: NotRequired["capo_mediaconvert.types.vp9_par_control.Vp9ParControl"]
    """Optional. Specify how the service determines the pixel aspect ratio for this output. The default behavior is to use the same pixel aspect ratio as your input video."""
    par_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33."""
    par_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40."""
    quality_tuning_level: NotRequired[
        "capo_mediaconvert.types.vp9_quality_tuning_level.Vp9QualityTuningLevel"
    ]
    """Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding."""
    rate_control_mode: NotRequired[
        "capo_mediaconvert.types.vp9_rate_control_mode.Vp9RateControlMode"
    ]
    """With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode."""


# --- restJson1 ser/de ---
def serialize_json(value: Vp9Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "framerate_control" in value:
        import capo_mediaconvert.types.vp9_framerate_control

        out["framerateControl"] = (
            capo_mediaconvert.types.vp9_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import capo_mediaconvert.types.vp9_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            capo_mediaconvert.types.vp9_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_size" in value:
        out["gopSize"] = value["gop_size"]
    if "hrd_buffer_size" in value:
        out["hrdBufferSize"] = value["hrd_buffer_size"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "par_control" in value:
        import capo_mediaconvert.types.vp9_par_control

        out["parControl"] = capo_mediaconvert.types.vp9_par_control.serialize_json(
            value["par_control"]
        )
    if "par_denominator" in value:
        out["parDenominator"] = value["par_denominator"]
    if "par_numerator" in value:
        out["parNumerator"] = value["par_numerator"]
    if "quality_tuning_level" in value:
        import capo_mediaconvert.types.vp9_quality_tuning_level

        out["qualityTuningLevel"] = (
            capo_mediaconvert.types.vp9_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    if "rate_control_mode" in value:
        import capo_mediaconvert.types.vp9_rate_control_mode

        out["rateControlMode"] = (
            capo_mediaconvert.types.vp9_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> Vp9Settings:
    out: Vp9Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "framerateControl" in data:
        import capo_mediaconvert.types.vp9_framerate_control

        out["framerate_control"] = (
            capo_mediaconvert.types.vp9_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import capo_mediaconvert.types.vp9_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            capo_mediaconvert.types.vp9_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "gopSize" in data:
        out["gop_size"] = data["gopSize"]
    if "hrdBufferSize" in data:
        out["hrd_buffer_size"] = data["hrdBufferSize"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "parControl" in data:
        import capo_mediaconvert.types.vp9_par_control

        out["par_control"] = capo_mediaconvert.types.vp9_par_control.deserialize_json(
            data["parControl"]
        )
    if "parDenominator" in data:
        out["par_denominator"] = data["parDenominator"]
    if "parNumerator" in data:
        out["par_numerator"] = data["parNumerator"]
    if "qualityTuningLevel" in data:
        import capo_mediaconvert.types.vp9_quality_tuning_level

        out["quality_tuning_level"] = (
            capo_mediaconvert.types.vp9_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    if "rateControlMode" in data:
        import capo_mediaconvert.types.vp9_rate_control_mode

        out["rate_control_mode"] = (
            capo_mediaconvert.types.vp9_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    return out
