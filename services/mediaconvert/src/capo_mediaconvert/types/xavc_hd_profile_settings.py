"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdProfileSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max1152000000
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min4_max12
    import capo_mediaconvert.types.xavc_flicker_adaptive_quantization
    import capo_mediaconvert.types.xavc_gop_b_reference
    import capo_mediaconvert.types.xavc_hd_profile_bitrate_class
    import capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level
    import capo_mediaconvert.types.xavc_hd_profile_telecine
    import capo_mediaconvert.types.xavc_interlace_mode


class XavcHdProfileSettings(TypedDict, closed=True):
    bitrate_class: NotRequired[
        "capo_mediaconvert.types.xavc_hd_profile_bitrate_class.XavcHdProfileBitrateClass"
    ]
    """Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
    flicker_adaptive_quantization: NotRequired[
        "capo_mediaconvert.types.xavc_flicker_adaptive_quantization.XavcFlickerAdaptiveQuantization"
    ]
    """The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides."""
    gop_b_reference: NotRequired[
        "capo_mediaconvert.types.xavc_gop_b_reference.XavcGopBReference"
    ]
    """Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames."""
    gop_closed_cadence: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting."""
    hrd_buffer_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max1152000000.__integerMin0Max1152000000"
    ]
    """Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point."""
    interlace_mode: NotRequired[
        "capo_mediaconvert.types.xavc_interlace_mode.XavcInterlaceMode"
    ]
    """Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose."""
    quality_tuning_level: NotRequired[
        "capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level.XavcHdProfileQualityTuningLevel"
    ]
    """Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
    slices: NotRequired[
        "capo_mediaconvert.types.__integer_min4_max12.__integerMin4Max12"
    ]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures."""
    telecine: NotRequired[
        "capo_mediaconvert.types.xavc_hd_profile_telecine.XavcHdProfileTelecine"
    ]
    """Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html."""


# --- restJson1 ser/de ---
def serialize_json(value: XavcHdProfileSettings) -> dict:
    out: dict = {}
    if "bitrate_class" in value:
        import capo_mediaconvert.types.xavc_hd_profile_bitrate_class

        out["bitrateClass"] = (
            capo_mediaconvert.types.xavc_hd_profile_bitrate_class.serialize_json(
                value["bitrate_class"]
            )
        )
    if "flicker_adaptive_quantization" in value:
        import capo_mediaconvert.types.xavc_flicker_adaptive_quantization

        out["flickerAdaptiveQuantization"] = (
            capo_mediaconvert.types.xavc_flicker_adaptive_quantization.serialize_json(
                value["flicker_adaptive_quantization"]
            )
        )
    if "gop_b_reference" in value:
        import capo_mediaconvert.types.xavc_gop_b_reference

        out["gopBReference"] = (
            capo_mediaconvert.types.xavc_gop_b_reference.serialize_json(
                value["gop_b_reference"]
            )
        )
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
    if "hrd_buffer_size" in value:
        out["hrdBufferSize"] = value["hrd_buffer_size"]
    if "interlace_mode" in value:
        import capo_mediaconvert.types.xavc_interlace_mode

        out["interlaceMode"] = (
            capo_mediaconvert.types.xavc_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "quality_tuning_level" in value:
        import capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level

        out["qualityTuningLevel"] = (
            capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "telecine" in value:
        import capo_mediaconvert.types.xavc_hd_profile_telecine

        out["telecine"] = (
            capo_mediaconvert.types.xavc_hd_profile_telecine.serialize_json(
                value["telecine"]
            )
        )
    return out


def deserialize_json(data: dict) -> XavcHdProfileSettings:
    out: XavcHdProfileSettings = {}  # type: ignore[typeddict-item]
    if "bitrateClass" in data:
        import capo_mediaconvert.types.xavc_hd_profile_bitrate_class

        out["bitrate_class"] = (
            capo_mediaconvert.types.xavc_hd_profile_bitrate_class.deserialize_json(
                data["bitrateClass"]
            )
        )
    if "flickerAdaptiveQuantization" in data:
        import capo_mediaconvert.types.xavc_flicker_adaptive_quantization

        out["flicker_adaptive_quantization"] = (
            capo_mediaconvert.types.xavc_flicker_adaptive_quantization.deserialize_json(
                data["flickerAdaptiveQuantization"]
            )
        )
    if "gopBReference" in data:
        import capo_mediaconvert.types.xavc_gop_b_reference

        out["gop_b_reference"] = (
            capo_mediaconvert.types.xavc_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if "gopClosedCadence" in data:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if "hrdBufferSize" in data:
        out["hrd_buffer_size"] = data["hrdBufferSize"]
    if "interlaceMode" in data:
        import capo_mediaconvert.types.xavc_interlace_mode

        out["interlace_mode"] = (
            capo_mediaconvert.types.xavc_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if "qualityTuningLevel" in data:
        import capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level

        out["quality_tuning_level"] = (
            capo_mediaconvert.types.xavc_hd_profile_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    if "slices" in data:
        out["slices"] = data["slices"]
    if "telecine" in data:
        import capo_mediaconvert.types.xavc_hd_profile_telecine

        out["telecine"] = (
            capo_mediaconvert.types.xavc_hd_profile_telecine.deserialize_json(
                data["telecine"]
            )
        )
    return out
