"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min0
    import aws_sdk_mediaconvert.types.__integer_min0_max15
    import aws_sdk_mediaconvert.types.__integer_min1_max32
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1000_max1152000000
    import aws_sdk_mediaconvert.types.__list_of_frame_metric_type
    import aws_sdk_mediaconvert.types.av1_adaptive_quantization
    import aws_sdk_mediaconvert.types.av1_bit_depth
    import aws_sdk_mediaconvert.types.av1_film_grain_synthesis
    import aws_sdk_mediaconvert.types.av1_framerate_control
    import aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm
    import aws_sdk_mediaconvert.types.av1_qvbr_settings
    import aws_sdk_mediaconvert.types.av1_rate_control_mode
    import aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization


class Av1Settings(TypedDict):
    adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.av1_adaptive_quantization.Av1AdaptiveQuantization"
    ]
    """Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization."""
    bit_depth: NotRequired["aws_sdk_mediaconvert.types.av1_bit_depth.Av1BitDepth"]
    """Specify the Bit depth. You can choose 8-bit or 10-bit."""
    film_grain_synthesis: NotRequired[
        "aws_sdk_mediaconvert.types.av1_film_grain_synthesis.Av1FilmGrainSynthesis"
    ]
    """Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor."""
    framerate_control: NotRequired[
        "aws_sdk_mediaconvert.types.av1_framerate_control.Av1FramerateControl"
    ]
    """Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm.Av1FramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    gop_size: NotRequired["aws_sdk_mediaconvert.types.__double_min0.__doubleMin0"]
    """Specify the GOP length (keyframe interval) in frames. With AV1, MediaConvert doesn't support GOP length in seconds. This value must be greater than zero and preferably equal to 1 + ((numberBFrames + 1) * x), where x is an integer value."""
    max_bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR."""
    number_b_frames_between_reference_frames: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """Specify from the number of B-frames, in the range of 0-15. For AV1 encoding, we recommend using 7 or 15. Choose a larger number for a lower bitrate and smaller file size; choose a smaller number for better video quality."""
    per_frame_metrics: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    qvbr_settings: NotRequired[
        "aws_sdk_mediaconvert.types.av1_qvbr_settings.Av1QvbrSettings"
    ]
    """Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode."""
    rate_control_mode: NotRequired[
        "aws_sdk_mediaconvert.types.av1_rate_control_mode.Av1RateControlMode"
    ]
    """'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.'"""
    slices: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max32.__integerMin1Max32"
    ]
    """Specify the number of slices per picture. This value must be 1, 2, 4, 8, 16, or 32. For progressive pictures, this value must be less than or equal to the number of macroblock rows. For interlaced pictures, this value must be less than or equal to half the number of macroblock rows."""
    spatial_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization.Av1SpatialAdaptiveQuantization"
    ]
    """Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher."""


# --- restJson1 ser/de ---
def serialize_json(value: Av1Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.av1_adaptive_quantization

        out["adaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.av1_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "bit_depth" in value:
        import aws_sdk_mediaconvert.types.av1_bit_depth

        out["bitDepth"] = aws_sdk_mediaconvert.types.av1_bit_depth.serialize_json(
            value["bit_depth"]
        )
    if "film_grain_synthesis" in value:
        import aws_sdk_mediaconvert.types.av1_film_grain_synthesis

        out["filmGrainSynthesis"] = (
            aws_sdk_mediaconvert.types.av1_film_grain_synthesis.serialize_json(
                value["film_grain_synthesis"]
            )
        )
    if "framerate_control" in value:
        import aws_sdk_mediaconvert.types.av1_framerate_control

        out["framerateControl"] = (
            aws_sdk_mediaconvert.types.av1_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_size" in value:
        out["gopSize"] = value["gop_size"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "number_b_frames_between_reference_frames" in value:
        out["numberBFramesBetweenReferenceFrames"] = value[
            "number_b_frames_between_reference_frames"
        ]
    if "per_frame_metrics" in value:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "qvbr_settings" in value:
        import aws_sdk_mediaconvert.types.av1_qvbr_settings

        out["qvbrSettings"] = (
            aws_sdk_mediaconvert.types.av1_qvbr_settings.serialize_json(
                value["qvbr_settings"]
            )
        )
    if "rate_control_mode" in value:
        import aws_sdk_mediaconvert.types.av1_rate_control_mode

        out["rateControlMode"] = (
            aws_sdk_mediaconvert.types.av1_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "spatial_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization

        out["spatialAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization.serialize_json(
                value["spatial_adaptive_quantization"]
            )
        )
    return out


def deserialize_json(data: dict) -> Av1Settings:
    out: Av1Settings = {}  # type: ignore[typeddict-item]
    if "adaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.av1_adaptive_quantization

        out["adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.av1_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if "bitDepth" in data:
        import aws_sdk_mediaconvert.types.av1_bit_depth

        out["bit_depth"] = aws_sdk_mediaconvert.types.av1_bit_depth.deserialize_json(
            data["bitDepth"]
        )
    if "filmGrainSynthesis" in data:
        import aws_sdk_mediaconvert.types.av1_film_grain_synthesis

        out["film_grain_synthesis"] = (
            aws_sdk_mediaconvert.types.av1_film_grain_synthesis.deserialize_json(
                data["filmGrainSynthesis"]
            )
        )
    if "framerateControl" in data:
        import aws_sdk_mediaconvert.types.av1_framerate_control

        out["framerate_control"] = (
            aws_sdk_mediaconvert.types.av1_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            aws_sdk_mediaconvert.types.av1_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "gopSize" in data:
        out["gop_size"] = data["gopSize"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "numberBFramesBetweenReferenceFrames" in data:
        out["number_b_frames_between_reference_frames"] = data[
            "numberBFramesBetweenReferenceFrames"
        ]
    if "perFrameMetrics" in data:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if "qvbrSettings" in data:
        import aws_sdk_mediaconvert.types.av1_qvbr_settings

        out["qvbr_settings"] = (
            aws_sdk_mediaconvert.types.av1_qvbr_settings.deserialize_json(
                data["qvbrSettings"]
            )
        )
    if "rateControlMode" in data:
        import aws_sdk_mediaconvert.types.av1_rate_control_mode

        out["rate_control_mode"] = (
            aws_sdk_mediaconvert.types.av1_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if "slices" in data:
        out["slices"] = data["slices"]
    if "spatialAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization

        out["spatial_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.av1_spatial_adaptive_quantization.deserialize_json(
                data["spatialAdaptiveQuantization"]
            )
        )
    return out
