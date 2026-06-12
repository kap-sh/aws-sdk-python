"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max128
    import aws_sdk_mediaconvert.types.__integer_min1_max1001
    import aws_sdk_mediaconvert.types.__integer_min24_max60000
    import aws_sdk_mediaconvert.types.__list_of_frame_metric_type
    import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings
    import aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings
    import aws_sdk_mediaconvert.types.xavc4k_profile_settings
    import aws_sdk_mediaconvert.types.xavc_adaptive_quantization
    import aws_sdk_mediaconvert.types.xavc_entropy_encoding
    import aws_sdk_mediaconvert.types.xavc_framerate_control
    import aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm
    import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings
    import aws_sdk_mediaconvert.types.xavc_hd_profile_settings
    import aws_sdk_mediaconvert.types.xavc_profile
    import aws_sdk_mediaconvert.types.xavc_slow_pal
    import aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization
    import aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization


class XavcSettings(TypedDict):
    adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_adaptive_quantization.XavcAdaptiveQuantization"
    ]
    """Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization."""
    entropy_encoding: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_entropy_encoding.XavcEntropyEncoding"
    ]
    """Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point."""
    framerate_control: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_framerate_control.XavcFramerateControl"
    ]
    """If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions."""
    framerate_conversion_algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm.XavcFramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max1001.__integerMin1Max1001"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Frame rate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min24_max60000.__integerMin24Max60000"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    per_frame_metrics: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    profile: NotRequired["aws_sdk_mediaconvert.types.xavc_profile.XavcProfile"]
    """Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC_HD_INTRA_CBG. To create an interlaced XAVC output, choose the profile XAVC_HD."""
    slow_pal: NotRequired["aws_sdk_mediaconvert.types.xavc_slow_pal.XavcSlowPal"]
    """Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25."""
    softness: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max128.__integerMin0Max128"
    ]
    """Ignore this setting unless your downstream workflow requires that you specify it explicitly. Otherwise, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video."""
    spatial_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization.XavcSpatialAdaptiveQuantization"
    ]
    """The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher."""
    temporal_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization.XavcTemporalAdaptiveQuantization"
    ]
    """The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization."""
    xavc4k_intra_cbg_profile_settings: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings.Xavc4kIntraCbgProfileSettings"
    ]
    """Required when you set Profile to the value XAVC_4K_INTRA_CBG."""
    xavc4k_intra_vbr_profile_settings: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings.Xavc4kIntraVbrProfileSettings"
    ]
    """Required when you set Profile to the value XAVC_4K_INTRA_VBR."""
    xavc4k_profile_settings: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_profile_settings.Xavc4kProfileSettings"
    ]
    """Required when you set Profile to the value XAVC_4K."""
    xavc_hd_intra_cbg_profile_settings: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings.XavcHdIntraCbgProfileSettings"
    ]
    """Required when you set Profile to the value XAVC_HD_INTRA_CBG."""
    xavc_hd_profile_settings: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_hd_profile_settings.XavcHdProfileSettings"
    ]
    """Required when you set Profile to the value XAVC_HD."""


# --- restJson1 ser/de ---
def serialize_json(value: XavcSettings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.xavc_adaptive_quantization

        out["adaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.xavc_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "entropy_encoding" in value:
        import aws_sdk_mediaconvert.types.xavc_entropy_encoding

        out["entropyEncoding"] = (
            aws_sdk_mediaconvert.types.xavc_entropy_encoding.serialize_json(
                value["entropy_encoding"]
            )
        )
    if "framerate_control" in value:
        import aws_sdk_mediaconvert.types.xavc_framerate_control

        out["framerateControl"] = (
            aws_sdk_mediaconvert.types.xavc_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "per_frame_metrics" in value:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "profile" in value:
        import aws_sdk_mediaconvert.types.xavc_profile

        out["profile"] = aws_sdk_mediaconvert.types.xavc_profile.serialize_json(
            value["profile"]
        )
    if "slow_pal" in value:
        import aws_sdk_mediaconvert.types.xavc_slow_pal

        out["slowPal"] = aws_sdk_mediaconvert.types.xavc_slow_pal.serialize_json(
            value["slow_pal"]
        )
    if "softness" in value:
        out["softness"] = value["softness"]
    if "spatial_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization

        out["spatialAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization.serialize_json(
                value["spatial_adaptive_quantization"]
            )
        )
    if "temporal_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization

        out["temporalAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization.serialize_json(
                value["temporal_adaptive_quantization"]
            )
        )
    if "xavc4k_intra_cbg_profile_settings" in value:
        import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings

        out["xavc4kIntraCbgProfileSettings"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings.serialize_json(
                value["xavc4k_intra_cbg_profile_settings"]
            )
        )
    if "xavc4k_intra_vbr_profile_settings" in value:
        import aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings

        out["xavc4kIntraVbrProfileSettings"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings.serialize_json(
                value["xavc4k_intra_vbr_profile_settings"]
            )
        )
    if "xavc4k_profile_settings" in value:
        import aws_sdk_mediaconvert.types.xavc4k_profile_settings

        out["xavc4kProfileSettings"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_settings.serialize_json(
                value["xavc4k_profile_settings"]
            )
        )
    if "xavc_hd_intra_cbg_profile_settings" in value:
        import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings

        out["xavcHdIntraCbgProfileSettings"] = (
            aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings.serialize_json(
                value["xavc_hd_intra_cbg_profile_settings"]
            )
        )
    if "xavc_hd_profile_settings" in value:
        import aws_sdk_mediaconvert.types.xavc_hd_profile_settings

        out["xavcHdProfileSettings"] = (
            aws_sdk_mediaconvert.types.xavc_hd_profile_settings.serialize_json(
                value["xavc_hd_profile_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> XavcSettings:
    out: XavcSettings = {}  # type: ignore[typeddict-item]
    if "adaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.xavc_adaptive_quantization

        out["adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.xavc_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if "entropyEncoding" in data:
        import aws_sdk_mediaconvert.types.xavc_entropy_encoding

        out["entropy_encoding"] = (
            aws_sdk_mediaconvert.types.xavc_entropy_encoding.deserialize_json(
                data["entropyEncoding"]
            )
        )
    if "framerateControl" in data:
        import aws_sdk_mediaconvert.types.xavc_framerate_control

        out["framerate_control"] = (
            aws_sdk_mediaconvert.types.xavc_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            aws_sdk_mediaconvert.types.xavc_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "perFrameMetrics" in data:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if "profile" in data:
        import aws_sdk_mediaconvert.types.xavc_profile

        out["profile"] = aws_sdk_mediaconvert.types.xavc_profile.deserialize_json(
            data["profile"]
        )
    if "slowPal" in data:
        import aws_sdk_mediaconvert.types.xavc_slow_pal

        out["slow_pal"] = aws_sdk_mediaconvert.types.xavc_slow_pal.deserialize_json(
            data["slowPal"]
        )
    if "softness" in data:
        out["softness"] = data["softness"]
    if "spatialAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization

        out["spatial_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.xavc_spatial_adaptive_quantization.deserialize_json(
                data["spatialAdaptiveQuantization"]
            )
        )
    if "temporalAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization

        out["temporal_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.xavc_temporal_adaptive_quantization.deserialize_json(
                data["temporalAdaptiveQuantization"]
            )
        )
    if "xavc4kIntraCbgProfileSettings" in data:
        import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings

        out["xavc4k_intra_cbg_profile_settings"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_settings.deserialize_json(
                data["xavc4kIntraCbgProfileSettings"]
            )
        )
    if "xavc4kIntraVbrProfileSettings" in data:
        import aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings

        out["xavc4k_intra_vbr_profile_settings"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_vbr_profile_settings.deserialize_json(
                data["xavc4kIntraVbrProfileSettings"]
            )
        )
    if "xavc4kProfileSettings" in data:
        import aws_sdk_mediaconvert.types.xavc4k_profile_settings

        out["xavc4k_profile_settings"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_settings.deserialize_json(
                data["xavc4kProfileSettings"]
            )
        )
    if "xavcHdIntraCbgProfileSettings" in data:
        import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings

        out["xavc_hd_intra_cbg_profile_settings"] = (
            aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_settings.deserialize_json(
                data["xavcHdIntraCbgProfileSettings"]
            )
        )
    if "xavcHdProfileSettings" in data:
        import aws_sdk_mediaconvert.types.xavc_hd_profile_settings

        out["xavc_hd_profile_settings"] = (
            aws_sdk_mediaconvert.types.xavc_hd_profile_settings.deserialize_json(
                data["xavcHdProfileSettings"]
            )
        )
    return out
