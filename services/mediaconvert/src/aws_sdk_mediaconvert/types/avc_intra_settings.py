"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max1001
    import aws_sdk_mediaconvert.types.__integer_min24_max60000
    import aws_sdk_mediaconvert.types.__list_of_frame_metric_type
    import aws_sdk_mediaconvert.types.avc_intra_class
    import aws_sdk_mediaconvert.types.avc_intra_framerate_control
    import aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm
    import aws_sdk_mediaconvert.types.avc_intra_interlace_mode
    import aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode
    import aws_sdk_mediaconvert.types.avc_intra_slow_pal
    import aws_sdk_mediaconvert.types.avc_intra_telecine
    import aws_sdk_mediaconvert.types.avc_intra_uhd_settings


class AvcIntraSettings(TypedDict, closed=True):
    avc_intra_class: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_class.AvcIntraClass"
    ]
    """Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling."""
    avc_intra_uhd_settings: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_uhd_settings.AvcIntraUhdSettings"
    ]
    """Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isn't allowed."""
    framerate_control: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_framerate_control.AvcIntraFramerateControl"
    ]
    """If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm.AvcIntraFramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max1001.__integerMin1Max1001"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min24_max60000.__integerMin24Max60000"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    interlace_mode: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_interlace_mode.AvcIntraInterlaceMode"
    ]
    """Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose."""
    per_frame_metrics: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    scan_type_conversion_mode: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode.AvcIntraScanTypeConversionMode"
    ]
    """Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive."""
    slow_pal: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_slow_pal.AvcIntraSlowPal"
    ]
    """Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25."""
    telecine: NotRequired[
        "aws_sdk_mediaconvert.types.avc_intra_telecine.AvcIntraTelecine"
    ]
    """When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""


# --- restJson1 ser/de ---
def serialize_json(value: AvcIntraSettings) -> dict:
    out: dict = {}
    if "avc_intra_class" in value:
        import aws_sdk_mediaconvert.types.avc_intra_class

        out["avcIntraClass"] = (
            aws_sdk_mediaconvert.types.avc_intra_class.serialize_json(
                value["avc_intra_class"]
            )
        )
    if "avc_intra_uhd_settings" in value:
        import aws_sdk_mediaconvert.types.avc_intra_uhd_settings

        out["avcIntraUhdSettings"] = (
            aws_sdk_mediaconvert.types.avc_intra_uhd_settings.serialize_json(
                value["avc_intra_uhd_settings"]
            )
        )
    if "framerate_control" in value:
        import aws_sdk_mediaconvert.types.avc_intra_framerate_control

        out["framerateControl"] = (
            aws_sdk_mediaconvert.types.avc_intra_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "interlace_mode" in value:
        import aws_sdk_mediaconvert.types.avc_intra_interlace_mode

        out["interlaceMode"] = (
            aws_sdk_mediaconvert.types.avc_intra_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "per_frame_metrics" in value:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "scan_type_conversion_mode" in value:
        import aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode

        out["scanTypeConversionMode"] = (
            aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode.serialize_json(
                value["scan_type_conversion_mode"]
            )
        )
    if "slow_pal" in value:
        import aws_sdk_mediaconvert.types.avc_intra_slow_pal

        out["slowPal"] = aws_sdk_mediaconvert.types.avc_intra_slow_pal.serialize_json(
            value["slow_pal"]
        )
    if "telecine" in value:
        import aws_sdk_mediaconvert.types.avc_intra_telecine

        out["telecine"] = aws_sdk_mediaconvert.types.avc_intra_telecine.serialize_json(
            value["telecine"]
        )
    return out


def deserialize_json(data: dict) -> AvcIntraSettings:
    out: AvcIntraSettings = {}  # type: ignore[typeddict-item]
    if "avcIntraClass" in data:
        import aws_sdk_mediaconvert.types.avc_intra_class

        out["avc_intra_class"] = (
            aws_sdk_mediaconvert.types.avc_intra_class.deserialize_json(
                data["avcIntraClass"]
            )
        )
    if "avcIntraUhdSettings" in data:
        import aws_sdk_mediaconvert.types.avc_intra_uhd_settings

        out["avc_intra_uhd_settings"] = (
            aws_sdk_mediaconvert.types.avc_intra_uhd_settings.deserialize_json(
                data["avcIntraUhdSettings"]
            )
        )
    if "framerateControl" in data:
        import aws_sdk_mediaconvert.types.avc_intra_framerate_control

        out["framerate_control"] = (
            aws_sdk_mediaconvert.types.avc_intra_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            aws_sdk_mediaconvert.types.avc_intra_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "interlaceMode" in data:
        import aws_sdk_mediaconvert.types.avc_intra_interlace_mode

        out["interlace_mode"] = (
            aws_sdk_mediaconvert.types.avc_intra_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if "perFrameMetrics" in data:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if "scanTypeConversionMode" in data:
        import aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode

        out["scan_type_conversion_mode"] = (
            aws_sdk_mediaconvert.types.avc_intra_scan_type_conversion_mode.deserialize_json(
                data["scanTypeConversionMode"]
            )
        )
    if "slowPal" in data:
        import aws_sdk_mediaconvert.types.avc_intra_slow_pal

        out["slow_pal"] = (
            aws_sdk_mediaconvert.types.avc_intra_slow_pal.deserialize_json(
                data["slowPal"]
            )
        )
    if "telecine" in data:
        import aws_sdk_mediaconvert.types.avc_intra_telecine

        out["telecine"] = (
            aws_sdk_mediaconvert.types.avc_intra_telecine.deserialize_json(
                data["telecine"]
            )
        )
    return out
