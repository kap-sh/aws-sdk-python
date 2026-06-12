"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max1152000000
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min8_max12
    import aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class
    import aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile
    import aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level
    import aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization
    import aws_sdk_mediaconvert.types.xavc_gop_b_reference


class Xavc4kProfileSettings(TypedDict):
    bitrate_class: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class.Xavc4kProfileBitrateClass"
    ]
    """Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
    codec_profile: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile.Xavc4kProfileCodecProfile"
    ]
    """Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH_422). These profiles are specified in ITU-T H.264."""
    flicker_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization.XavcFlickerAdaptiveQuantization"
    ]
    """The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides."""
    gop_b_reference: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_gop_b_reference.XavcGopBReference"
    ]
    """Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames."""
    gop_closed_cadence: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting."""
    hrd_buffer_size: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max1152000000.__integerMin0Max1152000000"
    ]
    """Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point."""
    quality_tuning_level: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level.Xavc4kProfileQualityTuningLevel"
    ]
    """Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
    slices: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min8_max12.__integerMin8Max12"
    ]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures."""


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kProfileSettings) -> dict:
    out: dict = {}
    if "bitrate_class" in value:
        import aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class

        out["bitrateClass"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class.serialize_json(
                value["bitrate_class"]
            )
        )
    if "codec_profile" in value:
        import aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile

        out["codecProfile"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile.serialize_json(
                value["codec_profile"]
            )
        )
    if "flicker_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization

        out["flickerAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization.serialize_json(
                value["flicker_adaptive_quantization"]
            )
        )
    if "gop_b_reference" in value:
        import aws_sdk_mediaconvert.types.xavc_gop_b_reference

        out["gopBReference"] = (
            aws_sdk_mediaconvert.types.xavc_gop_b_reference.serialize_json(
                value["gop_b_reference"]
            )
        )
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
    if "hrd_buffer_size" in value:
        out["hrdBufferSize"] = value["hrd_buffer_size"]
    if "quality_tuning_level" in value:
        import aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level

        out["qualityTuningLevel"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    return out


def deserialize_json(data: dict) -> Xavc4kProfileSettings:
    out: Xavc4kProfileSettings = {}  # type: ignore[typeddict-item]
    if "bitrateClass" in data:
        import aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class

        out["bitrate_class"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_bitrate_class.deserialize_json(
                data["bitrateClass"]
            )
        )
    if "codecProfile" in data:
        import aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile

        out["codec_profile"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_codec_profile.deserialize_json(
                data["codecProfile"]
            )
        )
    if "flickerAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization

        out["flicker_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.xavc_flicker_adaptive_quantization.deserialize_json(
                data["flickerAdaptiveQuantization"]
            )
        )
    if "gopBReference" in data:
        import aws_sdk_mediaconvert.types.xavc_gop_b_reference

        out["gop_b_reference"] = (
            aws_sdk_mediaconvert.types.xavc_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if "gopClosedCadence" in data:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if "hrdBufferSize" in data:
        out["hrd_buffer_size"] = data["hrdBufferSize"]
    if "qualityTuningLevel" in data:
        import aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level

        out["quality_tuning_level"] = (
            aws_sdk_mediaconvert.types.xavc4k_profile_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    if "slices" in data:
        out["slices"] = data["slices"]
    return out
